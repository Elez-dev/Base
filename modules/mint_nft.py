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
