import random
from modules.wallet import Wallet
from loguru import logger
from modules.retry import exception_handler
from web3 import Web3
from settings import QUANTITY
import json as js


class MintNFT(Wallet):
    def __init__(self, private_key, chain, number):
        super().__init__(private_key, chain, number)
        self.address = Web3.to_checksum_address('0x1d6b183bd47f914f9f1d3208edcf8befd7f84e63')
        self.abi = js.load(open('./abi/coin_earnings.txt'))
        self.contract = self.web3.eth.contract(address=self.address, abi=self.abi)

    @exception_handler('Mint Penny')
    def mint_penny(self):
        logger.info(f'Mint Penny NFT\n')
        tx = {
            'chainId': self.web3.eth.chain_id,
            'data': '0x1249c58b',
            'from': self.address_wallet,
            'to': Web3.to_checksum_address('0xb3da098a7251a647892203e0c256b4398d131a54'),
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'gas': 150_000,
            **self.get_gas_price()
        }

        gas = self.web3.eth.estimate_gas(tx)
        tx.update({'gas': gas})

        self.send_transaction_and_wait(tx, 'Mint Penny')

    @exception_handler('Mint COIN Earnings nft')
    def mint_coin_earnings(self):
        logger.info('Mint COIN Earnings nft')
        quantity = random.randint(QUANTITY[0], QUANTITY[1])
        if quantity == 0:
            return
        dick = {
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            **self.get_gas_price()
        }
        tx = self.contract.functions.claim(
            self.address_wallet,
            0,
            quantity,
            Web3.to_checksum_address('0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'),
            0,
            ([], 2, 0, Web3.to_checksum_address('0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE')),
            b'0x'
        ).build_transaction(dick)

        self.send_transaction_and_wait(tx, f'Mint {quantity} COIN Earnings nft')

    @exception_handler('Mint Why-Phi')
    def mint_philand(self):
        logger.info('Mint Why-Phi')
        data = '0x6a627842000000000000000000000000' + self.address_wallet[2:]
        tx = {
            'chainId': self.web3.eth.chain_id,
            'data': data,
            'from': self.address_wallet,
            'to': Web3.to_checksum_address('0xc649989246faa59bbefa7c65551cc4461e823320'),
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            'gas': 150_000,
            **self.get_gas_price()
        }

        gas = self.web3.eth.estimate_gas(tx)
        tx.update({'gas': gas})

        self.send_transaction_and_wait(tx, 'Mint Why-Phi')

    @exception_handler('Mint BASE PYTHON ZORB')
    def mint_python_zorb_base_opensea(self):
        logger.info('Mint BASE PYTHON ZORB')

        dick = {
            'from': self.address_wallet,
            'nonce': self.web3.eth.get_transaction_count(self.address_wallet),
            **self.get_gas_price()
        }

        contract = self.web3.eth.contract(address=Web3.to_checksum_address('0x00005ea00ac477b1030ce78506496e8c2de24bf5'), abi=js.load(open('./abi/opensea.txt')))
        txn = contract.functions.mintPublic(
            Web3.to_checksum_address('0x92dFC144B8B897d36E980e6E29217201801A1C1e'),
            Web3.to_checksum_address('0x0000a26b00c1F0DF003000390027140000fAa719'),
            Web3.to_checksum_address('0x0000000000000000000000000000000000000000'),
            1
        ).build_transaction(dick)

        self.send_transaction_and_wait(txn, f'Mint BASE PYTHON ZORB on OpenSea')



