from modules.chain import *

EXCEL_PASSWORD = False  # Если ставите пароль на Excel с приватниками || True/ False
SHUFFLE_WALLETS = True  # Перемешка кошельков                         || True/ False

TG_BOT_SEND = False  # Включить уведомления в тг или нет           || True/ False
TG_TOKEN = ''  # API токен тг-бота - создать его можно здесь - https://t.me/BotFather
TG_ID = 0  # id твоего телеграмма можно узнать тут       - https://t.me/getmyid_bot

CHAIN_RPC = {
    Base    : 'https://rpc.ankr.com/base',
}

MAX_GAS_ETH = 40        # gas в gwei (смотреть здесь : https://etherscan.io/gastracker)
BASE_GASPRICE = 0.001   # Использовать Max base fee и Priority fee для газа в Base

RETRY = 5  # Количество попыток при ошибках / фейлах
TIME_DELAY = [100, 200]  # Задержка после ТРАНЗАКЦИЙ     [min, max]
TIME_ACCOUNT_DELAY = [200, 300]  # Задержка между АККАУНТАМИ     [min, max]
TIME_DELAY_ERROR = [10, 20]  # Задержка при ошибках / фейлах [min, max]

# 1 - Mint Penny

QUANTITY_TRANS = [1, 2]  # [min, max]

# 2 - Mint COIN Earnings

QUANTITY = [1, 2]  # [min, max] Максимум можно только 2 на один акк