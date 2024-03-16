from modules import *
from settings import *
import json
from web3 import Web3
from loguru import logger

web3_eth = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth', request_kwargs={'timeout': 60}))


class CustomRouter:
    def __init__(self, private_key, number, proxy):
        self.number = number
        self.private_key = private_key
        self.proxy = proxy

    def mint_penny(self):
        nft = MintNFT(self.private_key, Base, self.number)
        nft.mint_penny()

    def mint_coin_earnings(self):
        nft = MintNFT(self.private_key, Base, self.number)
        nft.mint_coin_earnings()

    def mint_frames_of_the_fut(self):
        nft = MintNFT(self.private_key, Base, self.number)
        nft.mint_frames_of_the_future()

    def mint_eip4844(self):
        nft = MintFun(self.private_key, Base, self.number)
        nft.mint()

    def mint_boxs(self):
        nft = MintNFT(self.private_key, Base, self.number)
        nft.mint_box()

    def run(self):
        address = web3_eth.eth.account.from_key(self.private_key).address
        data = json.load(open('./data/router.json'))
        route = data[address]['route']
        index = data[address]['index']

        flag = False

        while index < len(route):
            method_name = route[index]
            if method_name is None:
                index += 1
                continue
            if hasattr(self, method_name):
                logger.info(f'Module - {method_name}\n')
                if hasattr(self, method_name):
                    method = getattr(self, method_name)
                    try:
                        method()
                        flag = True
                        logger.success(f'Module completed, sleep and move on to the next one\n')
                        sleeping(TIME_DELAY_ROUTES[0], TIME_DELAY_ROUTES[1])
                    except Exception as error:
                        logger.error(error)
                        continue
                    finally:
                        index += 1
                        data[address]['index'] = index
                        with open('./data/router.json', 'w') as f:
                            json.dump(data, f)
        else:
            return flag
