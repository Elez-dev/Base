from sys import stdout
from modules import *
from modules.custom_route import CustomRouter
from settings import ROUTES, TIME_ACCOUNT_DELAY, ROUTES_SHUFFLE, CHAIN_RPC, odos_token, TIME_DELAY
import time
import json

logger.remove()
logger.add("./data/log.txt")
logger.add(stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <7}</level> | <cyan>{message}</cyan>")
web3_eth = Web3(Web3.HTTPProvider(CHAIN_RPC['Ethereum'], request_kwargs={'timeout': 1}))


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
                nft.mint_philand()

            if self.action == 4:
                nft = MintNFT(key, Base, str_number)
                nft.mint_python_zorb_base_opensea()

            if self.action == 5:
                vote = RubyScore(key, Base, str_number)
                vote.vote()

            if self.action == 6:
                od = OdosSwap(key, Base, str_number, {})
                for token in odos_token:
                    res = od.sold_token(token)
                    if res is False:
                        continue
                    sleeping(TIME_DELAY[0], TIME_DELAY[1])

            if self.action == 8:
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
3 - Mint Why-Phi
4 - Mint Python Zorb opensea
5 - Vote on RubyScore
6 - Sold token Odos

7 - Generate Сustom routes (сначала запускаем этот модуль, потом модуль 7)
8 - Rus Сustom routes
''')

            time.sleep(0.1)
            act = int(input('Choose an action: '))

            if act == 7:
                Worker.generate_route()
                continue

            if act in range(1, 9):
                break

        worker = Worker(act)
        worker.work()
