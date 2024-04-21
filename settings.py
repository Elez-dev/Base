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
MAX_GAS_BASE = 0.2      # max gas в base (смотреть здесь : https://cointool.app/gasPrice/base)
SLIPPAGE = 1

RETRY = 2  # Количество попыток при ошибках / фейлах
TIME_DELAY = [100, 200]  # Задержка после ТРАНЗАКЦИЙ     [min, max]
TIME_ACCOUNT_DELAY = [2, 3]  # Задержка между АККАУНТАМИ     [min, max]
TIME_DELAY_ERROR = [10, 20]  # Задержка при ошибках / фейлах [min, max]

# 2 - Mint COIN Earnings

QUANTITY = [1, 2]  # [min, max] Максимум можно только 2 на один акк

# 6 - Sold Token

odos_token = [
    '0xb8d98a102b0079b69ffbc760c8d857a31653e56e'
]

# 8 - Custom routes

ROUTES = [
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
        'sold_token_odos'
'''

ROUTES_SHUFFLE = True           # Перемешка модулей
TIME_DELAY_ROUTES = [100, 200]  # Задержка между МОДУЛЯМИ     [min, max]
