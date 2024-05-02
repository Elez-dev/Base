import random
from loguru import logger
from web3 import Web3
from modules.retry import exception_handler
from modules.wallet import Wallet
import json as js

contracts = [
    {"address": "0x273cA93A52b817294830eD7572aA591Ccfa647fd"},
    {"address": "0xDeD6e72bdE74c7840fADE275c3afDb997be47BBf"},
    {"address": "0x398234D24388A47fd2c1c36097dEcb0364c7AFfC"},
    {"address": "0x28aBD603EeeC02B74fc2DBb1040694D40B9D4A0B"},
    {"address": "0x44bF3c538276b3D505D14ABEEE3E4480c3437C03"},
    {"address": "0x78721376b7c326A3EB99B89691e856285feD1aD1"},
    {"address": "0x774dc44f2F24915a435c5220c81584245b9a29F1"},
    {"address": "0xBCDAdD5780c5c80Ec53544AE96b3c8Af9F9550cf"},
    {"address": "0x0B7D6491A44bc47259D8918fBbBD08609E942967"},
    {"address": "0xc07a47493b5421E5EAb172e59E9f145b61bDCE9A"},
    {"address": "0x3aD1a7C0569A78BFCF3B49274bAb872a10070AD8"}, 
    {"address": "0x5b51Cf49Cb48617084eF35e7c7d7A21914769ff1"},
    
  ]


class MintFun(Wallet):

    def __init__(self, private_key, chain, number):
        super().__init__(private_key, chain, number)
        self.abi = js.load(open('./abi/mintfun.txt'))
