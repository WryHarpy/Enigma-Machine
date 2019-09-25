# PlugBoard.py
# Quang Hoang
# 24 Sept 2019

# PlugBoard for the Enigma Machine


import os
from requests import get
from bs4 import BeautifulSoup
   
    
# Open the letter set file and get the letter sets
    
with open ("LetterSet.xml") as file:
    char = BeautifulSoup (file, 'lxml')
    

def getSet(charSet):
    doc = eval("char.{}.text".format(charSet))
    set = []
    for i in doc:
        if i != '\n':
            set.append(i)
    #print(set)                
    return set


# Get the message
def getText():
    #text = input(str("Enter your message: "))
    replaceTextItems = [' ', '\n', '—', '-']
    #'''
    with open ("GettysburgAddress.txt", 'r') as text:
        text = text.read()
        print(text)
    #'''
    for i in replaceTextItems:
        text = text.replace(i, '')
    
    return text


# Run the scrambling and put it to a file
def runPlugBoard(text):
    letterSet = getSet("letterset")
    plugBoard = getSet("plugboard")
    
    # Check if the file is already exists
    if os.path.exists("encrypt message.txt"):
        os.remove("encrypt message.txt")
        file = open ("encrypt message.txt", 'a')
    else:
        file = open ("encrypt message.txt", 'a')
        
    # Append new message
    for i in text:
        index = letterSet.index(i)
        file.write(plugBoard[index])
    file.close()

# Re- write the message to file and screen
def writeMessage():
    file = open ("encrypt message.txt", 'r')
    file = file.read()    
    message = open ("encrypt message.txt", 'w')
    
    for i in range(0, len(file), 17):
        message.write(str(file[i:i+17]) + "  ")
        print (file[i:i+17], end= '   ')    


## M A I N ##     
runPlugBoard(getText())
writeMessage()
