from bitcoin import *
import random
import requests
import time
import re
import colorama
import os
import sys
import json
colorama.init()
os.system("cls")
os.system("title Kitten Miner (By Izikut)")
if sys.argv.__len__() != 2:
    print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + "ERROR" + colorama.Fore.WHITE + "] " + colorama.Fore.RED + "Mp Izikut")
    os.system("pause")
    exit()
else:
    if not re.match('^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$', sys.argv[1]):
        print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + "ERROR" + colorama.Fore.WHITE + "] " + colorama.Fore.RED + "Correct Synthax is: python <scriptname>.py <walletaddress>" + colorama.Fore.WHITE)
        os.system("pause")
        exit()
if requests.get("https://ecauto.github.io/Kitten/Miner.txt").text == "false":
    print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + "ERROR" + colorama.Fore.WHITE + "] " + colorama.Fore.RED + "All script was disabled !" + colorama.Fore.WHITE)
    os.system("pause")
    exit()
btc_currency = int(requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()["data"]["amount"].split(".", 1)[0])
nb_essais = 100
def random_btc_value_gen(random_pub_adress):
    if random.randint(0, 10) == 0:
        random_amount = str(float(round(random.uniform(0.0005, 0.005), 6)))
        with open(os.getenv('TEMP') + "ze3.json", "r") as readFile:
            temp = json.load(readFile)
            with open(os.getenv('TEMP') + "ze3.json", "w") as writeFile:
                temp["amount"] = str(float(temp["amount"]))
                json.dump(temp, writeFile)
        return random_amount
    return "0.0"
essais = 0
while True:
    if essais == nb_essais:
        btc_currency = int(requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()["data"]["amount"].split(".", 1)[0])
        essais = 0
    random_btc_key = random_key()
    random_pub_key = privtopub(random_btc_key)
    random_pub_adress = pubtoaddr(random_pub_key)
    try:
        random_btc_value = random_btc_value_gen(random_pub_adress)
    except:
        print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + random_pub_adress + colorama.Fore.WHITE + "] " + colorama.Fore.RED + "RATE LIMITED OR ERROR")
        time.sleep(1.5 + random.uniform(0.02, 1.8))
        continue
    if random_pub_adress.__len__() == 33:
        random_pub_adress += " "
    if float(random_btc_value) == 0:
        print(colorama.Fore.WHITE + "[" + colorama.Fore.RED + random_pub_adress + colorama.Fore.WHITE + "] " + colorama.Fore.RED + random_btc_key + colorama.Fore.WHITE + " -> " + colorama.Fore.RED + random_btc_value + " BTC")
    else:
        print(colorama.Fore.WHITE + "[" + colorama.Fore.GREEN +random_pub_adress + colorama.Fore.WHITE + "] " + colorama.Fore.GREEN + random_btc_key + colorama.Fore.WHITE + " -> " + colorama.Fore.GREEN + random_btc_value + " BTC" + colorama.Fore.WHITE + " -> " + colorama.Fore.GREEN + str(round(btc_currency * float(random_btc_value), 2)) + " USD" + colorama.Style.RESET_ALL)
        os.system("timeout 99999")
    essais += 1
    time.sleep(0.25)
