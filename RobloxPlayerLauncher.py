from argparse import ArgumentParser
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import unquote
from subprocess import Popen
from time import sleep,time
from os.path import dirname
from re import split
import colorama
from colorama import Fore #, Back, Style
from sys import exit,executable
from ctypes import windll
import requests
start_time = time()
windll.kernel32.SetConsoleTitleW("Launcher")
dir = dirname(executable)
parser = ArgumentParser()
parser.add_argument("a")
colorama.init(autoreset=True)
args = ""
version_launcher = "b'1'"
uf = urlopen("https://raw.githubusercontent.com/takoda121/Roblox-Launcher/main/Misc/version")
online_version = uf.read()
if (str(version_launcher) == str(online_version)):
    print(Fore.GREEN + "Launcher version is ok! ")
else:
    print(Fore.RED + "Download new update! ")
    Popen("start https://github.com/takoda121/Roblox-Launcher/releases")
    sleep(3)
    exit(0)
args = parser.parse_args().__str__()
print(Fore.BLUE + "Launcher by Take")
print("version: "+ Fore.YELLOW + dir.split("\\").pop() + "\n")
print("1: Normal Client")
print("2: Beta Client")
print("3: Update Roblox")
print("4: Headless Clients")
print("5: Exit")
xour = input()
if (xour == "1"):
    aoiwdjaow = split("\+",args)
    zigi = [split(":",_)[1] for _ in aoiwdjaow]
    args = "--InBrowser -t "+zigi[2]+" -j "+"\""+unquote(zigi[4])+"\""+" -b "+zigi[5]+" --launchtime="+zigi[3]+" --rloc "+zigi[6]+" --gloc "+zigi[7]+" -channel zflag"
    if dir.find("\\Roblox\\Versions\\version") == -1:
        exit(1)
    Popen(dir+"\\RobloxPlayerBeta.exe "+args)
if (xour == "2"):
    aoiwdjaow = split("\+",args)
    zigi = [split(":",_)[1] for _ in aoiwdjaow]
    argsu = "--app -t "+zigi[2]+" -j "+"\""+unquote(zigi[4])+"\""+" -b "+zigi[5]+" --launchtime="+zigi[3]+" --rloc "+zigi[6]+" --gloc "+zigi[7]+" -channel zflag"
    if dir.find("\\Roblox\\Versions\\version") == -1:
        exit(1)
    Popen(dir+"\\RobloxPlayerBeta.exe "+ argsu)
if (xour == "3"):
    print(Fore.RED + "Dont forget to put this launcher back!")
    Popen("start https://www.roblox.com/download/client")
if (xour == "4"):
    URL = "https://github.com/takoda121/Roblox-Launcher/raw/main/Misc/HeadLess.exe"
    response = requests.get(URL)
    open(dir+"headless.exe", "wb").write(response.content)
    print(Fore.RED+"OUR HEADLESS CLIENT MAY BE DETECTED BY YOUR AV")
    print(Fore.CYAN+"1:Normal Client\n2:Beta Client")
    papadapa =input()
    if (papadapa == "1"):
        print(Fore.YELLOW+"No anti-afk is implemented and you will need to terminate thru taskmgr")
        aoiwdjaow = split("\+",args)
        zigi = [split(":",_)[1] for _ in aoiwdjaow]
        args = "--InBrowser -t "+zigi[2]+" -j "+"\""+unquote(zigi[4])+"\""+" -b "+zigi[5]+" --launchtime="+zigi[3]+" --rloc "+zigi[6]+" --gloc "+zigi[7]+" -channel zflag"
        if dir.find("\\Roblox\\Versions\\version") == -1:
            exit(1)
        Popen(dir+"\\RobloxPlayerBeta.exe "+args)
        Popen(dir+"headless.exe")
    if (papadapa == "2"):
        print(Fore.YELLOW+"No anti-afk is implemented and you will need to terminate thru taskmgr")
        aoiwdjaow = split("\+",args)
        zigi = [split(":",_)[1] for _ in aoiwdjaow]
        args = "--app -t "+zigi[2]+" -j "+"\""+unquote(zigi[4])+"\""+" -b "+zigi[5]+" --launchtime="+zigi[3]+" --rloc "+zigi[6]+" --gloc "+zigi[7]+" -channel zflag"
        if dir.find("\\Roblox\\Versions\\version") == -1:
            exit(1)
        Popen(dir+"\\RobloxPlayerBeta.exe "+args)
        Popen(dir+"headless.exe")
if (xour == "5"):
    exit(0)
sleep(5)
exit(0)