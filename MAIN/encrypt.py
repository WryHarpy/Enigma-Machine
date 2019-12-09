# encrypt.py
# Quang Hoang
# 27 OCT 2019

# This is the encryption
import charSet
from Screens import *
from Utilities import getMessage, getKey


def encrypt():
    message, tempKey = encryption()
    key = tempKey.split("-")
    key = getKey(key)
    encryptMessage = []
    # Plugboard
    for s in range(len(message)):
        tempMess = ""
        for i in message[s]:
            inbound = charSet.letterSet
            outbound = charSet.plugBoard
            index = inbound.index(i)
            text = outbound[index]
            # Wheel 1
            for i in text:
                inbound = charSet.plugBoard
                outbound = eval("charSet.Rotor_{}".format(key[0]))
                index = inbound.index(i)
                text = outbound[index]
                # Wheel 2
                for i in text:
                    inbound = eval("charSet.Rotor_{}".format(key[0]))
                    outbound = eval("charSet.Rotor_{}".format(key[1]))
                    index = inbound.index(i)
                    text = outbound[index]
                    # Wheel 3
                    for i in text:
                        inbound = eval("charSet.Rotor_{}".format(key[1]))
                        outbound = eval("charSet.Rotor_{}".format(key[2]))
                        index = inbound.index(i)
                        tempMess = tempMess + outbound[index]
        encryptMessage.append(tempMess)
    return encryptMessage, tempKey


def encryptionMessage():
    docLines, key = getMessage(encrypt())
    option = str
    for i in range(len(docLines)):
        if i == len(docLines)-1:
            end = "Hit Enter or choose an option to proceed: "
            option = message(docLines[len(docLines)-1], key, end)
        else:
            end = "Hit Enter to continue..."
            message(docLines[i], key, end)
    return option

