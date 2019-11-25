# encrypt.py
# Quang Hoang
# 27 OCT 2019

# This is the encryption
import charSet
from Screens import *
from Utilities import getMessage


def encrypt():
    message, tempKey = encryption()
    print(message)
    print(tempKey)
    key = tempKey.split("-")
    encryptMessage = ''
    # Plugboard
    for i in message:
        inbound = charSet.letterSet
        outbound = charSet.plugBoard
        index = inbound.index(i)
        text = outbound[index]
        # Wheel 1
        for i in text:
            inbound = charSet.plugBoard
            outbound = eval("charSet.Rotor_{}".format(key[0]))
            index = inbound.index(i)
            text =  outbound[index]
            # Wheel 2
            for i in text:
                inbound = eval("charSet.Rotor_{}".format(key[0]))
                outbound = eval("charSet.Rotor_{}".format(key[1]))
                index = inbound.index(i)
                text =  outbound[index]
                # Wheel 3
                for i in text:
                    inbound = eval("charSet.Rotor_{}".format(key[1]))
                    outbound = eval("charSet.Rotor_{}".format(key[2]))
                    index = inbound.index(i)
                    encryptMessage = encryptMessage + outbound[index]
    return encryptMessage, tempKey

def encryptionMessage():
    docLines, key = getMessage(encrypt())
    option = message(docLines, key)
    return option

