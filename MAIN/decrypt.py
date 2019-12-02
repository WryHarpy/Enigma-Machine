import charSet
from Screens import *
from Utilities import getKey


def decrypt():
    message, tempKey = decryption()
    message = message.replace("  ", "")
    key = tempKey.split("-")
    key = getKey(key)
    decryptMessage = ''
    # Wheel 3
    for i in message:
        inbound = eval("charSet.Rotor_{}".format(key[2]))
        outbound = eval("charSet.Rotor_{}".format(key[1]))
        index = inbound.index(i)
        text = outbound[index]
        # Wheel 2
        for i in text:
            inbound = eval("charSet.Rotor_{}".format(key[1]))
            outbound = eval("charSet.Rotor_{}".format(key[0]))
            index = inbound.index(i)
            text =  outbound[index]
            # Wheel 1
            for i in text:
                inbound = eval("charSet.Rotor_{}".format(key[0]))
                outbound = charSet.plugBoard
                index = inbound.index(i)
                text =  outbound[index]
                # Plugboard
                for i in text:
                    inbound = charSet.plugBoard
                    outbound = charSet.letterSet
                    index = inbound.index(i)
                    decryptMessage = decryptMessage + outbound[index]
    return decryptMessage, tempKey


def decryptionMessage():
    docLines = []
    doc, key = decrypt()
    for i in range(0, len(doc), 60):
        docLines.append("          " + doc[i:i+60] + "          \n")
    option = message(docLines, key)
    return option
