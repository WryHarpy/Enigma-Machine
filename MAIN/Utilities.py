# Utilities.py
# Quang Hoang
# 21 OCT 2019

# Some handy tools

from Screens import error
from charSet import letterSet
import re
import MAIN


# ###########################################################################################################################################################################
# Open the letter set file and get the letter sets
def getSet(charSet):
    doc = open(charSet, 'r')
    set = doc.read()
    return set

# ###########################################################################################################################################################################
# Re- write the message to file and screen
def writeMessage():
    file = open("encrypt message.txt", 'r')
    file = file.read()
    message = open("encrypt message.txt", 'w')

    for i in range(0, len(file), 17):
        message.write(str(file[i:i + 17]) + "  ")
        print(file[i:i + 17], end='   ')


# ###########################################################################################################################################################################
# Get the message
def getText():
    # text = input(str("Enter your message: "))
    replaceTextItems = [' ', '\n', '—', '-']
    # '''
    with open("GettysburgAddress.txt", 'r') as text:
        text = text.read()
        print(text)
    # '''
    for i in replaceTextItems:
        text = text.replace(i, '')
    return text


# ###########################################################################################################################################################################
# Write message into a text file doc.txt. This write lines to fit the screen
def writeDoc(message):
    #message = open("message.txt", 'r')
    #message = message.read()
    doc = open("doc.txt", 'w')
    for i in range(0, len(message), 60):
        doc.write("       " + message[i:i + 15] + "  " + message[i + 15:i + 30] + "  " + message[i + 30:i + 45] + "  " + message[i + 45:i + 60] + "       \n")
    doc.close()


# ###########################################################################################################################################################################
# Get the text from doc.txt
def getDoc():
    f = open("doc.txt", 'r')
    doc = f.readlines()
    f.close()
    return doc


# ###########################################################################################################################################################################
# Put the message into an array
def getMessage(message):
    messList, key = message
    doc = []
    count = 0
    for message in messList:
        for i in range(0, len(message), 60):
            if len(doc) < count + 1:
                doc.insert(count, [])
            doc[count].append("       " + message[i:i + 15] + "  " + message[i + 15:i + 30] + "  " + message[i + 30:i + 45] + "  " + message[i + 45:i + 60] + "       ")
            if len(doc[count]) == 9:
                count += 1
    return doc, key


# ###########################################################################################################################################################################
def getKey(key):
    from primeNumbers import primeNumbers
    temp = []
    count = 1
    for i in key:
        num = primeNumbers[eval(i)]
        for i in range(num):
            if count == 3:
                count = 1
            else:
                count += 1
        temp.append(str(count))
        count = 1

    return temp


# ###########################################################################################################################################################################
def checkPath(path):
    import os
    doc = path
    if os.path.exists(doc):
        f = open(doc, 'r')
        doc = f.read()
    return doc


# ###########################################################################################################################################################################
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


# ###########################################################################################################################################################################
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

