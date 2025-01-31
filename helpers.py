from web3 import Web3
import re
import requests
import os
from dotenv import load_dotenv

load_dotenv()

ALCHEMY_URL = os.getenv("ALCHEMY_URL")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))

def is_smart_contract(address):
    #  Returns True if the address is a smart contract, False if it's a normal wallet.
    bytecode = w3.eth.get_code(Web3.to_checksum_address(address))
    return len(bytecode) > 2  # Empty bytecode is '0x'


def is_too_many_transactions(address):
    ETHERSCAN_URL = "https://api.etherscan.io/api"

    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": ETHERSCAN_API_KEY
    }

    try:
        response = requests.get(ETHERSCAN_URL, params=params, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()

        if data.get("status") != "1" or "result" not in data:
            logging.warning(f"Unexpected response from Etherscan: {data}")
            return False

        total_transactions = len(data["result"])
        return total_transactions >= 10_000 

    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

    return False  # Default to False in case of errors
