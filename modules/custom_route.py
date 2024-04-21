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

    def mint_philand(self):
        nft = MintNFT(self.private_key, Base, self.number)
        nft.mint_philand()

    def mint_python_zorb_opensea(self):
        nft = MintNFT(self.private_key, Base, self.number)
        nft.mint_python_zorb_base_opensea()

    def vote_rubyscore(self):
        vote = RubyScore(self.private_key, Base, self.number)
        vote.vote()

    def sold_token_odos(self):
        od = OdosSwap(self.private_key, Base, self.number, {})
        for token in odos_token:
            res = od.sold_token(token)
            if res is False:
                continue
            sleeping(TIME_DELAY[0], TIME_DELAY[1])

    def run(self):
        address = web3_eth.eth.account.from_key(self.private_key).address
        data = json.load(open('./data/router.json'))
        try:
            route = data[address]['route']
            index = data[address]['index']
        except:
            return False

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
