# Program: screen_MAIN.py
# Author : Quang Hoang
# Date   : 2019-10-07
# Synopis: This run a screen when called


from Screens import *
import os


class Screen:

    def __init__(self, scr, op1, op2, op3, op4, op5, op6):

        self.scr = scr
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.op5 = op5
        self.op6 = op6

    def viewScr(self):
        os.system("clear")
        option = self.scr()

        return option


def getOption(x):
    os.system("clear")

    option = eval(str(x)).viewScr()

    try:
        if option == "1":
            getOption(eval(x).op1)
        if option == "2":
            getOption(eval(x).op2)
        if option == "3":
            getOption(eval(x).op3)
        if option == "4":
            getOption(eval(x).op4)
        if option == "5":
            getOption(eval(x).op5)
        if option == "6":
            getOption(eval(x).op6)
        else:
            getOption(x)
    except AttributeError or TypeError:
        getOption(x)


# ################# SET UP SCREEN #################
Welcome = Screen(WelScr, None, None,
               "Help",
               "Setting", None, None)

About = Screen(about, None, None, None, None, None, None)

Menu = Screen(menu,
            "Welcome",
            "About", None, None,
            "Setting",
            "Help")

Setting = Screen(setting,
               "Rotor_1",
               "Rotor_2",
               "Rotor_3",
               "PlugBoard",
               "Key", None)

Rotor_1 = Screen(settingRotor_1, None, None, None, None, None, None)
Rotor_2 = Screen(settingRotor_2, None, None, None, None, None, None)
Rotor_3 = Screen(settingRotor_3, None, None, None, None, None, None)
PlugBoard = Screen(settingPlugBoard, None, None, None, None, None, None)
Key = Screen(settingKey, None, None, None, None, None, None)
Help = Screen(helpScr, None, None, None, None, None, None)
Instruction = Screen(instructions, None, None, None, None, None, None)


# >>>>>>>>>>>>>>>>> M A I N <<<<<<<<<<<<<<<<<
os.system("clear")
about()
getOption("Menu")
