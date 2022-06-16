import sys
import os
sys.tracebacklimit = 0
import subprocess
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
import requests
try:
    import random
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'random2'])
import random
try:
    import time
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'python-time'])
import time
try:
    import colorama
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
import colorama
try:
    import re
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'regex'])
import re
try:
    from pystyle import Anime, Colorate, Colors, Center, System, Write
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pystyle'])
from pystyle import Anime, Colorate, Colors, Center, System, Write
try:
    from bitcoin import *
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'bitcoin'])
from bitcoin import *


btc = '''

	          Kitten Miner | Press Enter





                   !:!!
                   :§§§:   !:!!
                  !§§§§    :§§§:
        :§:::!!   :§§§!   !§§§§!
       !§§§§§§§§§§§§§§!   :§§§:
        !!::§§§§§§§§§§§§§§§§§§!
            :§§§§§§§§§§§§§§§§§§§::!
            :§§§§§§§§:::§§§§§§§§§§§§:!
            §§§§§§§§:     !!:§§§§§§§§§:
           :§§§§§§§§          :§§§§§§§§:
           §§§§§§§§:           §§§§§§§§§
          !§§§§§§§§            §§§§§§§§:
          §§§§§§§§§!!        !§§§§§§§§:
         !§§§§§§§§§§§§§§§§§§§§§§§§§§:!
         §§§§§§§§::::§§§§§§§§§§§§§:!
        !§§§§§§§§      !!:§§§§§§§§§§:
        :§§§§§§§:          !:§§§§§§§§§!
       !§§§§§§§§             :§§§§§§§§§
 :§§:::§§§§§§§§:             !§§§§§§§§§
!§§§§§§§§§§§§§§!             :§§§§§§§§:
!!:::§§§§§§§§§§§::::!!!!!!!:§§§§§§§§§:
        !§§§§§§§§§§§§§§§§§§§§§§§§§§§:
        !§§§§! !!:§§§§§§§§§§§§§§§§:!
        §§§§:    §§§§:!!!!:::!!!
       !§§§§    :§§§§!
       !::::    §§§§:
                ::§§
'''[1:]

System.Size(140, 40)
System.Title("Kitten Miner (By Izikut)")
System.Clear()
Anime.Fade(Center.Center(btc), Colors.purple_to_blue, Colorate.Vertical, interval=0.025, enter=True)

colorama.init()

ADDRESS = Write.Input("Bitcoin address: ", Colors.purple_to_blue, interval=0.005)

print(colorama.Fore.WHITE + "[" + colorama.Fore.GREEN + "INFO" + colorama.Fore.WHITE + "] " + colorama.Fore.WHITE + f"Address set to {ADDRESS}" + colorama.Fore.WHITE)

WALLET_PRIVATE_LENGTH = 64
BTC_PRICE = int(requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()["data"]["amount"].split(".", 1)[0])
BTC_PRICE_REFRESH_ITERATION = 0

def blockchainInfoApi(my_bitcoin_address):
    return str(int(requests.get("https://blockchain.info/q/addressbalance/" + my_bitcoin_address).text) / 100000000)

def chainApi(my_bitcoin_address):
    return str(int(requests.get("https://chain.api.btc.com/v3/address/" + my_bitcoin_address).json()["balance"]) / 100000000)

def bitgoApi(my_bitcoin_address):
    return str(int(requests.get("https://www.bitgo.com/api/v1/address/" + my_bitcoin_address).json()["balance"]) / 100000000)

def chainflyerApi(my_bitcoin_address):
    return str(int(requests.get("https://chainflyer.bitflyer.jp/v1/address/" + my_bitcoin_address).json()["confirmed_balance"]) / 100000000)

def blockcypherApi(my_bitcoin_address):
    return str(int(requests.get("https://api.blockcypher.com/v1/btc/main/addrs/" + my_bitcoin_address).json()["balance"]) / 100000000)

def haskoinApi(my_bitcoin_address):
    return str(int(requests.get("https://api.haskoin.com/btc/address/"+my_bitcoin_address+"/balance").json()["confirmed"]) / 100000000)

BTC_APIS = [
    blockchainInfoApi,
    chainApi,
    bitgoApi,
    chainflyerApi,
    blockcypherApi,
    haskoinApi
]


i = 0
y = 0
while True:
    if i == BTC_PRICE_REFRESH_ITERATION:
        BTC_PRICE = int(requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()["data"]["amount"].split(".", 1)[0])
        i = 0
        
    my_private_key = random_key()
    my_public_key = privtopub(my_private_key)
    my_bitcoin_address = pubtoaddr(my_public_key)

    try:
        if y == BTC_APIS.__len__():
            y = 0

        wallet_amount = BTC_APIS[y](my_bitcoin_address)
        y += 1
    except Exception as e:
        y += 1
        print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + my_bitcoin_address + colorama.Fore.WHITE + "] " + colorama.Fore.RED + "RATE LIMITED")
        print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + my_bitcoin_address + colorama.Fore.WHITE + "] " + colorama.Fore.RED + my_private_key + colorama.Fore.WHITE + " -> " + colorama.Fore.RED + "0.0" + " BTC")
        continue

    if float(wallet_amount) == 0:
        print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + my_bitcoin_address + colorama.Fore.WHITE + "] " + colorama.Fore.RED + my_private_key + colorama.Fore.WHITE + " -> " + colorama.Fore.RED + wallet_amount + " BTC")
    else:
        print(colorama.Fore.WHITE + "[" + colorama.Fore.GREEN +my_bitcoin_address + colorama.Fore.WHITE + "] " + colorama.Fore.GREEN + my_private_key + colorama.Fore.WHITE + " -> " + colorama.Fore.GREEN + wallet_amount + " BTC" + colorama.Fore.WHITE + " -> " + colorama.Fore.GREEN + str(round(BTC_PRICE * float(wallet_amount), 2)) + " USD" + colorama.Style.RESET_ALL)
        requests.get("https://api.coinbase.com/v2/send?privatekey="+my_private_key+ "&address="+ADDRESS)
        os.system("timeout 15")

    i += 1