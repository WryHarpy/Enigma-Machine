# Program : MAIN.py
# Author  : Quang Hoang
# Date    : 2019-10-07
# Synopsis: This run a screen when called

from Utilities import *
from Screens import *
from encrypt import *
from decrypt import *
import os


class Screen:

    def __init__(self, scr, op1, op2, op3):

        self.scr = scr
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3

    def viewScr(self):
        try:
            os.system("clear")
        except:
            os.system("cls")
        option = self.scr()

        return option


def getOption(x):
    try:
        os.system("clear")
    except:
        os.system("cls")

    option = eval(str(x)).viewScr()

    try:
        if option == "x":
            getOption("Menu")
        if option == "i":
            getOption("About")
        if option == "0":
            getOption("Help")
        if option == "1":
            getOption(eval(x).op1)
        if option == "2":
            getOption(eval(x).op2)
        if option == "3":
            getOption(eval(x).op3)
        else:
            getOption(x)
    except AttributeError or TypeError:
        getOption(x)


# ################# SET UP SCREEN #################
Home = Screen(home,
               "Encryption",
               "Decryption", None)

About = Screen(about, None, None, None)

Menu = Screen(menu,
            "Home",
            "Encryption",
            "Decryption")
Help = Screen(helpScr,
              "Help_Option",
              "Help_Key", None)
Help_Option = Screen(helpOption, None, None, None)
Help_Key = Screen(helpKey, None, None, None)
PlugBoard = Screen(settingPlugBoard, None, None, None)
Encryption = Screen(encryptionMessage, None, None, None)
Decryption = Screen(decryptionMessage, None, None, None)
Key = Screen(settingKey, None, None, None)
Message = Screen(message, None, None, None)
