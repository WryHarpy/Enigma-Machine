from Wheels import w1, w2, w3
def encryption():
    print('This is the encryption side')
    inbound= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    outbound = w1
    word = input('enter the word you want to encrypt:')
    wordOut = ''
    for i in range(len(word)):
        count = 0
        for j in range(len(inbound)):
            if (word[i] == inbound[j]):
                count = j
        wordOut = wordOut + outbound[count]
    print(wordOut)
#Second Wheel
    inbound = outbound
    outbound = w2 
    word = wordOut
    wordOut = ''
    for i in range(len(word)):
        count = 0
        for j in range(len(inbound)):
            if (word[i] == inbound[j]):
                count = j
        wordOut = wordOut + outbound[count]
    print(wordOut) 
#Third Wheel
    inbound = outbound
    outbound = w3 
    word = wordOut

    wordOut = ''
    for i in range(len(word)):
        count = 0
        for j in range(len(inbound)):
            if (word[i] == inbound[j]):
                count = j
        wordOut = wordOut + outbound[count]
    print(wordOut)
def decryption():
    print('This is the decryption side')
    inbound= w3
    outbound = w2
    word = input('enter the word you want to decrypt:')
    wordOut = ''
    for i in range(len(word)):
        count = 0
        for j in range(len(inbound)):
            if (word[i] == inbound[j]):
                count = j
        wordOut = wordOut + outbound[count]
    print(wordOut)
#Second Wheel
    inbound = outbound
    outbound = w1 
    word = wordOut
    wordOut = ''
    for i in range(len(word)):
        count = 0
        for j in range(len(inbound)):
            if (word[i] == inbound[j]):
                count = j
        wordOut = wordOut + outbound[count]
    print(wordOut) 
#Third Wheel
    inbound = outbound
    outbound = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    word = wordOut

    wordOut = ''
    for i in range(len(word)):
        count = 0
        for j in range(len(inbound)):
            if (word[i] == inbound[j]):
                count = j
        wordOut = wordOut + outbound[count]
    print(wordOut)     
#Calling
answer = '0'
while answer == '0':
    print('Press 1 for encrypt, or 2 for decrypt.')
    answer = input()
    if answer == '1':
        encryption()
    if answer == '2':
        decryption()
    else:
        answer = '0'
        continue
