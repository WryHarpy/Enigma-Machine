# process_MAIN.py
# Quang Hoang
# 21 OCT 2019

# This is the processor of the Encryption

import generateKey
import charSet


key = generateKey.getKey()
def encryption():
    text = input("Enter message: ")

    # Append new message
    for i in text:
        inbound = charSet.charSet["letterSet"]
        outbound = charSet.charSet["plugBoard"]

        index = inbound.index(i)
        wordOut = outbound[index]

        for k in key:
            inbound = outbound
            outbound = charSet.charSet["Rotor_{}".format(k)]
            for x in wordOut:
                index = inbound.index(x)
                wordOut = outbound[index]
        print(wordOut, end='')

    k = ''
    for i in key:
        k = k + str(i)
    print("\nKey: " + k)
