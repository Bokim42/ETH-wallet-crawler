import helpers
import requests
import os
from dotenv import load_dotenv

load_dotenv()

DUNE_API_KEY = os.getenv("DUNE_API_KEY")
BASE_DUNE_API_URL = "https://api.dune.com/api/echo/v1/transactions/evm/"

visited_addresses = set()
direct_interaction_wallets = set()
indirect_interaction_wallets = set()

def get_transactions(eth_address):

    visited_addresses.add(eth_address)

    if helpers.is_smart_contract(eth_address) or helpers.is_too_many_transactions(eth_address): # no transactions query for smart contracts or high transaction wallets
        return []

    DUNE_API_URL = BASE_DUNE_API_URL + eth_address
    headers = {"X-Dune-Api-Key": DUNE_API_KEY}
    params = {"chain_ids": ["1"]}  # Only ETH network
    
    all_transactions = []
    next_offset = None

    while next_offset is not None or not all_transactions:
        if next_offset:
            params["offset"] = next_offset
        
        response = requests.get(DUNE_API_URL, headers=headers, params=params)
        data = response.json()
        
        transactions = data.get("transactions", [])
        if not transactions:
            break

        all_transactions.extend(transactions)
        next_offset = data.get("next_offset")

    return all_transactions

def extract_addresses_from_transactions(transactions):
    new_addresses = set()
    for tx in transactions:
        data = tx.get("data", "")
        if data == "0x" or data.startswith("0xa9059cbb"):
            if tx.get("transaction_type") == "Receiver":
                new_addresses.add(tx.get("from"))
            elif tx.get("transaction_type") == "Sender":
                new_addresses.add(tx.get("to"))
    return new_addresses

def crawl_wallets(initial_eth_address):
    global direct_interaction_wallets, indirect_interaction_wallets
    
    print(f"Crawling direct transfers for {initial_eth_address}")
    direct_transactions = get_transactions(initial_eth_address)
    direct_interaction_wallets = extract_addresses_from_transactions(direct_transactions)
    
    print(f"Found {len(direct_interaction_wallets)} direct interaction wallets. Crawling second hop...")
    for wallet in direct_interaction_wallets:
        if wallet not in visited_addresses:
            transactions = get_transactions(wallet)
            indirect_addresses = extract_addresses_from_transactions(transactions)
            indirect_interaction_wallets.update(indirect_addresses)
    
    print(f"Found {len(indirect_interaction_wallets)} indirect wallets.")

def main():
    eth_address = input("Enter Ethereum address: ").strip()

    crawl_wallets(eth_address)
    
    print("Direct Interaction Wallets:", direct_interaction_wallets)
    print("Indirect Interaction Wallets:", indirect_interaction_wallets)

if __name__ == "__main__":
    main()