import random
from loguru import logger
from web3 import Web3
from modules.retry import exception_handler
from modules.wallet import Wallet
import json as js

contracts = [
    {"address": "0x273cA93A52b817294830eD7572aA591Ccfa647fd"}
  ]


class MintFun(Wallet):

    def __init__(self, private_key, chain, number):
        super().__init__(private_key, chain, number)
        self.abi = js.load(open('./abi/mintfun.txt'))
