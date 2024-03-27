from modules.chain import *

EXCEL_PASSWORD = False  # Если ставите пароль на Excel с приватниками || True/ False
SHUFFLE_WALLETS = True  # Перемешка кошельков                         || True/ False

TG_BOT_SEND = False  # Включить уведомления в тг или нет           || True/ False
TG_TOKEN = ''  # API токен тг-бота - создать его можно здесь - https://t.me/BotFather
TG_ID = 0  # id твоего телеграмма можно узнать тут       - https://t.me/getmyid_bot

CHAIN_RPC = {
    Ethereum: 'https://rpc.ankr.com/eth',
    Base    : 'https://rpc.ankr.com/base',
}

MAX_GAS_ETH = 400        # max gas в gwei (смотреть здесь : https://etherscan.io/gastracker)
MAX_GAS_BASE = 5      # max gas в base (смотреть здесь : https://cointool.app/gasPrice/base)

RETRY = 2  # Количество попыток при ошибках / фейлах
TIME_DELAY = [100, 200]  # Задержка после ТРАНЗАКЦИЙ     [min, max]
TIME_ACCOUNT_DELAY = [200, 300]  # Задержка между АККАУНТАМИ     [min, max]
TIME_DELAY_ERROR = [10, 20]  # Задержка при ошибках / фейлах [min, max]

# 2 - Mint COIN Earnings

QUANTITY = [1, 2]  # [min, max] Максимум можно только 2 на один акк

# 3 - Custom routes

ROUTES = [
    ['mint_penny', None],
    ['mint_coin_earnings', None],
    ['mint_philand'],
    ['mint_python_zorb_opensea'],
    ['vote_rubyscore']
]
'''
    Список доступных модулей
        'mint_penny'
        'mint_coin_earnings'
        'mint_philand'
        'mint_python_zorb_opensea'
        'vote_rubyscore'
'''

ROUTES_SHUFFLE = True           # Перемешка модулей
TIME_DELAY_ROUTES = [100, 200]  # Задержка между МОДУЛЯМИ     [min, max]
