from web3 import Web3
from loguru import logger
from sys import stdout
from settings import *
from modules.func import shuffle, get_accounts_data, sleeping
from modules.mint_nft import MintNFT
import time

logger.remove()
logger.add("./data/log.txt")
logger.add(stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <7}</level> | <cyan>{message}</cyan>")
web3_eth = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth', request_kwargs={'timeout': 60}))


class Worker:
    def __init__(self, action):
        self.action = action

    @staticmethod
    def chek_gas_eth():
        while True:
            try:
                res = int(round(Web3.from_wei(web3_eth.eth.gas_price, 'gwei')))
                logger.info(f'Газ сейчас - {res} gwei\n')
                if res <= MAX_GAS_ETH:
                    break
                else:
                    time.sleep(60)
                    continue
            except Exception as error:
                logger.error(error)
                time.sleep(30)
                continue

    def work(self):
        i = 0
        for number, key in keys_list:
            str_number = f'{number} / {all_wallets}'
            i += 1
            address = web3_eth.eth.account.from_key(key).address
            logger.info(f'Account #{i} || {address}\n')
            self.chek_gas_eth()

            if self.action == 1:
                nft = MintNFT(key, Base, str_number)
                nft.mint_penny()

            if self.action == 2:
                nft = MintNFT(key, Base, str_number)
                nft.mint_coin_earnings()

            logger.success(f'Account completed, sleep and move on to the next one\n')
            sleeping(TIME_ACCOUNT_DELAY[0], TIME_ACCOUNT_DELAY[1])


if __name__ == '__main__':
    list1 = get_accounts_data()
    all_wallets = len(list1)
    logger.info(f'Number of wallets: {all_wallets}\n')
    keys_list = shuffle(list1)

    while True:
        while True:
            logger.info('''
1 - Mint Penny
2 - Mint COIN Earnings
''')

            time.sleep(0.1)
            act = int(input('Choose an action: '))

            if act in range(1, 3):
                break

        worker = Worker(act)
        worker.work()
