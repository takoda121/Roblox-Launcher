from argparse import ArgumentParser
from multiprocessing.spawn import old_main_modules
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import unquote
from subprocess import Popen
from time import sleep,time
from os.path import dirname
from re import split
from click import command
import colorama
from colorama import Fore #, Back, Style
from sys import exit,executable
from ctypes import windll
from requests import get as rget
import requests
#import setuptools
import tkinter
import webbrowser
import tkinter.messagebox
import customtkinter
#import discord_webhook
from json import loads
customtkinter.set_default_color_theme("green") #"blue" "green" "dark-blue" "sweetkind"
dir = dirname(executable)
colorama.init(autoreset=True)
version_launcher = "2"
cuk = rget("https://raw.githubusercontent.com/takoda121/Roblox-Launcher/main/Misc/version")
ovst3 = cuk.text
ufur = rget("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag") #setup.roblox/version doesnt work for me so im using this trash
ufurjget = loads(ufur.text)
RBXonline_version = ufurjget['clientVersionUpload']
print("Roblox official version: " + RBXonline_version)
print("Online version: " + ovst3 + " Your version: " + version_launcher)
parser = ArgumentParser()
parser.add_argument("a")
args = parser.parse_args().__str__()
aoiwdjaow = split("\+",args)
zigi = [split(":",_)[1] for _ in aoiwdjaow]
placeId = args.split("placeId%3D")[1].split("%26isPlayTogetherGame")[0]
universeidreq = loads(rget(f'https://api.roblox.com/universes/get-universe-containing-place?placeid='+placeId).text)
universeId = universeidreq["UniverseId"]
sleep(0.3)
reqpalceghne = loads(rget(f'https://games.roblox.com/v1/games?universeIds='+str(universeId)).text)
placeName = reqpalceghne["data"][0]["name"]
if (str(version_launcher) == ovst3 or float(ovst3)<float(version_launcher)):
    print(Fore.GREEN +"Launcher version is ok! ")
else:
    print(Fore.RED + "Download new update! ") #Fore.RED + 
    webbrowser.open("https://github.com/takoda121/Roblox-Launcher/releases")
    windll.user32.MessageBoxW(0, "Download New Launcher Update " + version_launcher + " -> " + ovst3, "Launcher", 1)
    sleep(3)
    exit(0)
class App(customtkinter.CTk):

    WIDTH = 1000
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Launcher V" + version_launcher)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="LAUNCHER By Take V"+version_launcher,
                                              text_font=("Roboto Medium", -16)) 
        self.label_1.grid(row=1, column=0, pady=10, padx=10)
        installedrobloxver = dir.split("\\").pop()
        nugurcolo = "green"
        nugurtextour = ""
        if (installedrobloxver == RBXonline_version):
            nugurcolo = "green"
            nugurtextour = installedrobloxver
        else:
            nugurcolo = "red"
            nugurtextour = installedrobloxver + " Update to " + RBXonline_version

        self.label_2 = customtkinter.CTkLabel(master=self.frame_right,
                                              text=nugurtextour,
                                              text_font=("Roboto Medium", -16),
                                              text_color = nugurcolo)  
        self.label_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Normal Client",
                                                command=self.normal_client)
        self.button_1.grid(row=3, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Beta Client",
                                                command=self.beta_client)
        self.button_2.grid(row=4, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Normal Client HL",
                                                command=self.normal_client_headless)
        self.button_3.grid(row=5, column=0, pady=10, padx=20)
        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Beta Client HL",
                                                command=self.beta_client_headless)
        self.button_4.grid(row=6, column=0, pady=10, padx=20)
        self.button_6a = customtkinter.CTkButton(master=self.frame_left,
                                                text="Update Roblox",
                                                command=self.update_roblox)
        self.button_6a.grid(row=8, column=0, pady=10, padx=20)
        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Unhide HL",
                                                command=self.un_headless)
        self.button_5.grid(row=7, column=0, pady=10, padx=20)
        self.changinglaubel = customtkinter.CTkLabel(master=self.frame_right,
                                              text="V"+version_launcher,
                                              text_font=("Roboto Medium", -16))
        self.changinglaubel.grid(row=1, column=0, pady=10, padx=10)
        self.GAMELABEL = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Joining: "+placeName,
                                              text_font=("Roboto Medium", -16),
                                              text_color = "cyan")
        self.GAMELABEL.grid(row=2, column=0, pady=10, padx=20)

    def button_event(self):
        print("Button pressed")

    def normal_client(self):
        self.changinglaubel.configure(text="This is the best option! Many exploits work only on this!")


        args = "--InBrowser -t "+zigi[2]+" -j "+"\""+unquote(zigi[4])+"\""+" -b "+zigi[5]+" --launchtime="+zigi[3]+" --rloc "+zigi[6]+" --gloc "+zigi[7]+" -channel zflag"
        if dir.find("\\Roblox\\Versions\\version") == -1:
            exit(1)
        Popen(dir+"\\RobloxPlayerBeta.exe "+args)
        sleep(5)
        exit(0)
    def update_roblox(self):
        URL = "https://www.roblox.com/download/client"
        response = rget(URL)
        open(dir+"\\"+dir.split("\\").pop()+"updater.exe", "wb").write(response.content)
        Popen(dir+"\\"+dir.split("\\").pop()+"updater.exe")
    def normal_client_headless(self):
        URL = "https://github.com/takoda121/Roblox-Launcher/raw/main/Misc/HeadLess.exe"
        response = rget(URL)
        open(dir+"\\headless.exe", "wb").write(response.content)
        self.changinglaubel.configure(text="You will not be able to see anything on the screen! Might be flagged on your AV!")
        aoiwdjaow = split("\+",args)
        zigi = [split(":",_)[1] for _ in aoiwdjaow]
        args = "--InBrowser -t "+zigi[2]+" -j "+"\""+unquote(zigi[4])+"\""+" -b "+zigi[5]+" --launchtime="+zigi[3]+" --rloc "+zigi[6]+" --gloc "+zigi[7]+" -channel zflag"
        if dir.find("\\Roblox\\Versions\\version") == -1:
            exit(1)
        Popen(dir+"\\RobloxPlayerBeta.exe "+args)
        Popen(dir+"\\headless.exe")
    def beta_client_headless(self):
        URL = "https://github.com/takoda121/Roblox-Launcher/raw/main/Misc/HeadLess.exe"
        response = rget(URL)
        open(dir+"\\headless.exe", "wb").write(response.content)
        self.changinglaubel.configure(text="You will not be able to see anything on the screen! Might be flagged on your AV!")
        aoiwdjaow = split("\+",args)
        zigi = [split(":",_)[1] for _ in aoiwdjaow]
        args = "--app -t "+zigi[2]+" -j "+"\""+unquote(zigi[4])+"\""+" -b "+zigi[5]+" --launchtime="+zigi[3]+" --rloc "+zigi[6]+" --gloc "+zigi[7]+" -channel zflag"
        if dir.find("\\Roblox\\Versions\\version") == -1:
            exit(1)
        Popen(dir+"\\RobloxPlayerBeta.exe "+args)
        Popen(dir+"\\headless.exe")
    def un_headless(self):
        URL = "https://github.com/takoda121/Roblox-Launcher/raw/main/Misc/UnHeadLess.exe"
        response = rget(URL)
        open(dir+"\\unheadless.exe", "wb").write(response.content)
        Popen(dir+"\\unheadless.exe")
    def beta_client(self):
        self.changinglaubel.configure(text="This is the default client only some exploits work with it!")
        aoiwdjaow = split("\+",args)
        zigi = [split(":",_)[1] for _ in aoiwdjaow]
        args = "--app -t "+zigi[2]+" -j "+"\""+unquote(zigi[4])+"\""+" -b "+zigi[5]+" --launchtime="+zigi[3]+" --rloc "+zigi[6]+" --gloc "+zigi[7]+" -channel zflag"
        if dir.find("\\Roblox\\Versions\\version") == -1:
            exit(1)
        Popen(dir+"\\RobloxPlayerBeta.exe "+args)
        sleep(5)
        exit(0)
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    start_time = time()
    nuge = App()
    nuge.mainloop()
