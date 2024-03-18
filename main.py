from wallets import wallets
import web3
from web3 import Web3
import sys
from config import *


def check_balance(chain, address):
    link = rpc[chain]
    connect = Web3(web3.HTTPProvider(link))
    balance = connect.eth.get_balance(address)
    return balance / 10 ** 18


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <chain> <address>")
        sys.exit(1)

    chain = sys.argv[1]
    address = sys.argv[2]

    res = check_balance(chain, address)
    print(res)
