# Program : MAIN.py
# Author  : Quang Hoang
# Date    : 2019-10-07
# Synopsis: This run a screen when called

from Utilities import *
from Screens import *
from encrypt import encryptionMessage
from decrypt import decryptionMessage
import os


class Screen:

    def __init__(self, scr, op1, op2, op3, op4):

        self.scr = scr
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4

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
        if option == "4":
            getOption(eval(x).op4)
        else:
            getOption(x)
    except AttributeError or TypeError:
        getOption(x)


# ################# SET UP SCREEN #################
Home = Screen(home,
               "Encryption",
               "Decryption", None, None)

About = Screen(about, None, None, None, None)

Menu = Screen(menu,
            "Home",
            "Encryption",
            "Decryption",
            "Exit")
Help = Screen(helpScr,
              "Help_Option",
              "Help_Key", None, None)
Help_Option = Screen(helpOption, None, None, None, None)
Help_Key = Screen(helpKey, None, None, None, None)
PlugBoard = Screen(settingPlugBoard, None, None, None, None)
Encryption = Screen(encryptionMessage, None, None, None, None)
Decryption = Screen(decryptionMessage, None, None, None, None)
Key = Screen(settingKey, None, None, None, None)
Message = Screen(message, None, None, None, None)
Exit = Screen(closePGR, None, None, None, None)
