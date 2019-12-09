import charSet
from Screens import *
from Utilities import getKey


def decrypt():
    message, tempKey = decryption()
    key = tempKey.split("-")
    key = getKey(key)
    decryptMessage = []
    # Wheel 3
    for s in range(len(message)):
        tempMess = ""
        for i in message[s]:
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
                        tempMess = tempMess + outbound[index]
        decryptMessage.append(tempMess)
    return decryptMessage, tempKey


def getMessage(message):
    messList, key = message
    doc = []
    count = 0
    for message in messList:
        for i in range(0, len(message), 60):
            if len(doc) < count + 1:
                doc.insert(count, [])
            doc[count].append("          " + message[i:i + 60] + "          ")
            if len(doc[count]) == 9:
                count += 1
    return doc, key


def decryptionMessage():
    doc, key = getMessage(decrypt())
    option = str
    for i in range(len(doc)):
        if i == len(doc)-1:
            end = "Hit Enter or choose an option to proceed: "
            option = message(doc[len(doc)-1], key, end)
        else:
            end = "Hit Enter to continue..."
            message(doc[i], key, end)
    return option
