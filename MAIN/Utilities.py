# Utilities.py
# Quang Hoang
# 21 OCT 2019

# Some handy tools

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
    message, key = message
    doc = []
    for i in range(0, len(message), 60):
        doc.append("       " + message[i:i + 15] + "  " + message[i + 15:i + 30] + "  " + message[i + 30:i + 45] + "  " + message[i + 45:i + 60] + "       \n")
    return doc, key


# ###########################################################################################################################################################################
def getKey(key):
    from primeNumbers import primeNumbers
    temp = []
    for i in key:
        i = primeNumbers[eval(i)]%3
        temp.append(str(i))

    return temp


