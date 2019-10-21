'''
   takes in my inbound string and converts it to my outbound string.   
'''
inbound= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
outbound = 'ZNFKMEAXYGDHUCPTSRVLOIWJQB'
#########################DECRYPTS 
temp = outbound
outbound = inbound
inbound = temp
word = input('enter the word you want to Decrypt:')
wordOut = ''
for i in range(len(word)):
    count = 0
    for j in range(len(inbound)):
        if (word[i] == inbound[j]):
            count = j
    wordOut = wordOut + outbound[count]
print(wordOut) 
#############ENCRYPTS


wordOut = '' # this is the word I am going to toss out.  
for i in range(len(word)):
    count = 0
    for j in range(len(inbound)):
        if (word[i] == inbound[j]):
            count = j
    wordOut = wordOut + outbound[count]
print(wordOut)
