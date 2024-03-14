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

    @exception_handler('Mint on MintFun')
    def mint(self):
        conract = random.choice(contracts)
        contr = self.web3.eth.contract(address=Web3.to_checksum_address(conract["address"]), abi=self.abi)
        name = contr.functions.name().call()
        logger.info(f'Mint {name} on MintFun')

        dick = {
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            **self.get_gas_price()
        }

        contract_txn = contr.functions.mint().build_transaction(dick)
        self.send_transaction_and_wait(contract_txn, f'Mint {name} on MintFun')