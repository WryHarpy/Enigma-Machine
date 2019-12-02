'''
Program: checkKey.py
Author : Quang Hoang
Date   : 2019-12-2
Synopis: This module will check for the wrong key format
'''

import re
from Screens import error
import MAIN


def checkKey(key,scr):
    pattern = re.compile(r'^(\d|\d\d|\d\d\d)\-(\d|\d\d|\d\d\d)\-(\d|\d\d|\d\d\d)$')
    match = pattern.match(key)

    if key == "":
        error("No key inputted")
        MAIN.getOption(scr)
    if match:
        tempKey = key.split("-")
        for i in tempKey:
            x = eval(i)
            if type(x) == int:
                if 0 < x or x < 665:
                    pass
                if 0 > x or x > 665:
                    error("Out of Range: {}".format(key))
                    MAIN.getOption(scr)
            if type(x) != int:
                error("Invalid Number Range: {}".format(key))
                MAIN.getOption(scr)

    if not match:
        error("Wrong Key Format: {}".format(key))
        MAIN.getOption(scr)

