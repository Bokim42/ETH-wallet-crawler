The Ethereum wallet crawler performs two levels of network analysis:

1. Direct Transfers: It identifies wallets that have directly sent ETH or ERC20 tokens to a specified target wallet.
2. Secondary Connections: It then maps out additional wallets that have transacted with those initial direct transfer wallets, expanding the network of related addresses.


Its using Dune API, Etherescan API, Alchemy with web3.py library.

## Usage

Run the main function to start crawling Ethereum addresses:
```
python crawl_wallets.py
```
You will be prompted to enter an Ethereum address:
```
Enter Ethereum address: 0xec70bd334d2177c014ae7aafead527412dbab5f8
```

Output example:
```
Crawling direct transfers for 0xec70bd334d2177c014ae7aafead527412dbab5f8
Found 7 direct interaction wallets. Crawling second hop...
Found 37 indirect wallets.
Direct Interaction Wallets: {'0x14599a862ec5a61003af233d3e977f40e8cf1f91', '0xbb76ced3c2b7c2a8bdbf2731e24132fae47f0b9c', '0x89f210b01a007d0d6950181d63878c6f39897cdb', '0xd27109666f353c9b09ed37e2d20bc0108f7deec5', '0x171a96d67f8d52b38a38d9cc57222bebbd293bb8', '0x4e1b6cdc068adc36ae492cc6e2d296a63cfe1f9d', '0xdac17f958d2ee523a2206206994597c13d831ec7'}
Indirect Interaction Wallets: {'0x14599a862ec5a61003af233d3e977f40e8cf1f91', '0x145a922dee6b6fd6b607ae044a0518e8e0af1f91', '0xffed821d457841dc361fd4ca642d94c7ac8b6462', '0x969dee8943a6243bd8de4048a72c2607ef396434', '0x46340b20830761efd32832a74d7169b29feb9758', '0x6b02e83722b4ba309ddf629be23e2acb62398fae', '0x561b1a2750d8596603e01215f8bdbef184a379e3', '0x7bbb162cb14478642c380a21e2025ba205796830', '0x4e1b6cdc068adc36ae492cc6e2d296a63cfe1f9d', '0x5f8bfd9c957ebaad33fbc99c2add9f87d4f19d93', '0x9642b23ed1e01df1092b92641051881a322f5d4e', '0xbb76ced3c2b7c2a8bdbf2731e24132fae47f0b9c', '0xe291cc3e5b9e0c9b37c9fbdd549abf3b5c0ad342', '0x969ddfcb6f379f74cab5066611441b25c5176434', '0xd27109666f353c9b09ed37e2d20bc0108f7deec5', '0x73fe0ca051a383ab33f610425db71038e4643fc2', '0x4f88f272fe5ab5eefd6004b640b4e7bc76a0b304', '0xf1c9cac3160423ea01aeac562843228c58d38d63', '0x270423e2fbc82d13f1bc7ddc65807094786cf803', '0x963737c550e70ffe4d59464542a28604edb2ef9a', '0xa4abf225e4896ee8db18990f2a12f320d050ef35', '0x969d77f867767aed74e0cf3cd441bc868e066434', '0xe6620ec2fe041b12ff1bd730bb8a0f33200e4db7', '0x479454068cca3920c571261330802eb8d7c1ac0e', '0x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88', '0x22cb840b2a56617830b41ea753bca6b317ba56d0', '0xdac17f958d2ee523a2206206994597c13d831ec7', '0xbbe4cb957344441e4e66b79cae226a1e422e9ac0', '0x4976a4a02f38326660d17bf34b431dc6e2eb2327', '0x1459d30b2d0497d628eee41b858d7915a5bf1f91', '0x6b4dd800746adb11862ed704efc8d01f927f8a28', '0x14594a0feeedfdaaccf4ba02c3e9013c9e2e1f91', '0x969deab0152159d38c94e7170f71970a93c76434', '0x21beca18d9377e61a39d1baf3ee0caf184479305', '0x89f210b01a007d0d6950181d63878c6f39897cdb', '0x45300136662dd4e58fc0df61e6290dffd992b785', '0xec70bd334d2177c014ae7aafead527412dbab5f8'}
```
