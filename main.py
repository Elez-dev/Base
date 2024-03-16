import random
from sys import stdout
from modules import *
from modules.custom_route import CustomRouter
from settings import ROUTES, TIME_ACCOUNT_DELAY, ROUTES_SHUFFLE
import time
import json

logger.remove()
logger.add("./data/log.txt")
logger.add(stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <7}</level> | <cyan>{message}</cyan>")
web3_eth = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth', request_kwargs={'timeout': 60}))


class Worker:
    def __init__(self, action):
        self.action = action

    @staticmethod
    def generate_route():
        dick = {}
        for number, key in keys_list:

            address = web3_eth.eth.account.from_key(key).address
            new_routes = []

            if ROUTES_SHUFFLE is True:
                random.shuffle(ROUTES)

            for subarray in ROUTES:
                if isinstance(subarray, list):
                    new_routes.append(random.choice(subarray))
                elif isinstance(subarray, str):
                    new_routes.append(subarray)
                else:
                    new_routes.append(None)

            dick[address] = {
                'index': 0,
                'route': new_routes
            }

        with open('./data/router.json', 'w') as f:
            json.dump(dick, f)

        logger.success('Successfully generated route\n')

    def work(self):
        i = 0
        for number, key in keys_list:
            str_number = f'{number} / {all_wallets}'
            i += 1
            address = web3_eth.eth.account.from_key(key).address
            logger.info(f'Account #{i} || {address}\n')

            if self.action == 1:
                nft = MintNFT(key, Base, str_number)
                nft.mint_penny()

            if self.action == 2:
                nft = MintNFT(key, Base, str_number)
                nft.mint_coin_earnings()

            if self.action == 3:
                nft = MintNFT(key, Base, str_number)
                nft.mint_frames_of_the_future()

            if self.action == 4:
                nft = MintFun(key, Base, str_number)
                nft.mint()

            if self.action == 5:
                nft = MintNFT(key, Base, str_number)
                nft.mint_box()

            if self.action == 7:
                router = CustomRouter(key, str_number, {})
                res = router.run()
                if res is False:
                    continue

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
1 - Mint Penny NFT (1 на акк)
2 - Mint COIN Earnings NFT(максимум 2 на аккаунт)
3 - Mint Frames of the Future (1 за транзакцию)
4 - EIP-4844 is Based (1 за транзакцию)
5 - Mint Box

6 - Generate Сustom routes (сначала запускаем этот модуль, потом модуль 7)
7 - Rus Сustom routes
''')

            time.sleep(0.1)
            act = int(input('Choose an action: '))

            if act == 6:
                Worker.generate_route()
                continue

            if act in range(1, 8):
                break

        worker = Worker(act)
        worker.work()
