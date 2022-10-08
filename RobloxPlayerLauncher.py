from argparse import ArgumentParser
from urllib.request import urlopen
from urllib.parse import unquote
from subprocess import Popen
from time import sleep,time
from os.path import dirname
from re import split
from os import system
import colorama
from colorama import Fore #, Back, Style
from sys import exit,executable
from ctypes import windll
import webbrowser
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
    print(Fore.GREEN + "Version is ok! ")
else:
    print(Fore.RED + "Download new update! ")
    system("start https://github.com/takoda121/Roblox-Launcher/releases")
    sleep(3)
    exit(0)
args = parser.parse_args().__str__()
print(Fore.BLUE + "Launcher by Take")
print("version: "+ Fore.YELLOW + dir.split("\\").pop())
print("") #Works as a newline
print("1: Normal Client")
print("2: Beta Client")
print("3: Update Roblox")
print("4: Exit")
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
    webbrowser.open("https://www.roblox.com/download/client")
if (xour == "4"):
    exit(0)
sleep(5)
exit(0)