'''
Program: messageProcess.py
Author : Quang Hoang
Date   : 2019-10-07
Synopis: This will check and clean up input message and return a list of message
'''

from Utilities import checkPath, checkDoc

def messageProcess(message, crnScreen):
    message = checkPath(message)
    message = message.replace("  ", "")
    message = message.split("\n")
    temp = []
    for i in message:
        i = i.strip()
        checkDoc(i, crnScreen)
        temp.append(i)
    message = temp
    return message

