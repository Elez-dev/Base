from modules.chain import *

EXCEL_PASSWORD = False  # Если ставите пароль на Excel с приватниками || True/ False
SHUFFLE_WALLETS = True  # Перемешка кошельков                         || True/ False

TG_BOT_SEND = False  # Включить уведомления в тг или нет           || True/ False
TG_TOKEN = ''  # API токен тг-бота - создать его можно здесь - https://t.me/BotFather
TG_ID = 0  # id твоего телеграмма можно узнать тут       - https://t.me/getmyid_bot

CHAIN_RPC = {
    Base    : 'https://rpc.ankr.com/base',
}

MAX_GAS_ETH = 400        # gas в gwei (смотреть здесь : https://etherscan.io/gastracker)
BASE_GASPRICE = 0.05   # Использовать Max base fee и Priority fee для газа в Base

RETRY = 1  # Количество попыток при ошибках / фейлах
TIME_DELAY = [100, 200]  # Задержка после ТРАНЗАКЦИЙ     [min, max]
TIME_ACCOUNT_DELAY = [200, 300]  # Задержка между АККАУНТАМИ     [min, max]
TIME_DELAY_ERROR = [10, 20]  # Задержка при ошибках / фейлах [min, max]

# 2 - Mint COIN Earnings

QUANTITY = [1, 2]  # [min, max] Максимум можно только 2 на один акк

# 3 - Custom routes

ROUTES = [
    ['mint_penny'],
    ['mint_coin_earnings'],
    ['mint_frames_of_the_fut'],
    ['mint_eip4844']
]
'''
    Список доступных модулей
        'mint_penny'
        'mint_coin_earnings'
        'mint_frames_of_the_fut'
        'mint_eip4844'
           
    Disclaimer - You can add modules to [] to select random ones,
    example [module_1, module_2, [module_3, module_4], module 5]
    The script will start with module 1, 2, 5 and select a random one from module 3 and 4

    You can also specify None in [], and if None is selected by random, this module will be skipped
'''

ROUTES_SHUFFLE = True           # Перемешка модулей
TIME_DELAY_ROUTES = [100, 200]  # Задержка между МОДУЛЯМИ     [min, max]
