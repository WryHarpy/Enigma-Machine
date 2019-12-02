'''
Program: checkDoc.py
Author : Quang Hoang
Date   : 2019-11-24
Synopis: This module will check for the invalid character
'''

from Screens import error
from charSet import letterSet


def checkDoc(doc,scr):
    invalidChar = ""
    for i in doc:
        if i in letterSet:
            pass
        if i not in letterSet:
            if i not in invalidChar:
                invalidChar = invalidChar + i

    if invalidChar != "":
        error("Invalid character: {}".format(invalidChar))
        import MAIN
        MAIN.getOption(scr)

