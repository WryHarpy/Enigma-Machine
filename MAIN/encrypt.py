# encrypt.py
# Quang Hoang
# 27 OCT 2019

# This is the encryption
import generateKey
import charSet
from Screens import *
from Utilities import getMessage


key = generateKey.getKey()
def encrypt():
    text = encryption()
    print(text)
    encryptMessage = ''
    for i in text:
        inbound = charSet.charSet["letterSet"]
        outbound = charSet.charSet["plugBoard"]
        index = inbound.index(i)
        encryptMessage = encryptMessage + outbound[index]
        #wordOut = outbound[index]

    print(encryptMessage)
    return encryptMessage
'''
        for k in key:
            inbound = outbound
            outbound = charSet.charSet["Rotor_{}".format(k)]
            for x in wordOut:
                index = inbound.index(x)
                encryptMessage = encryptMessage + outbound[index]
        #print(wordOut, end='')
'''


def encryptionMessage():
    docLines = getMessage(encrypt())
    option = message(docLines)
    return option

