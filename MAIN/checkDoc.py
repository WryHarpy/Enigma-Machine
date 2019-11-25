'''
Program: checkDoc.py
Author : Quang Hoang
Date   : 2019-11-24
Synopis: This module will check for the invalid character
'''

from charSet import letterSet

def checkDoc(doc):
    invalidChar = ""
    for i in doc:
        if i in letterSet:
            pass
        if i not in letterSet:
            invalidChar = invalidChar + i

    return invalidChar



