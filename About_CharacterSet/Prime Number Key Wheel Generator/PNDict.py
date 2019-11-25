# Nick Demanche
# 18 November 2019
# CIS220 - Object Oriented Programming
# Prime Number Dictionary Builder

import random

def getFile(fileName):
    finalList = []
    fO = open(fileName, 'r')
    theList = fO.readlines()
    fO.close()
    for i in range(len(theList)):
        word = ''
        tl = theList[i]
        for k in range(0, len(tl)):  # removes the line Number
            word = word + tl[k]
        word = word.replace('\n', '')
        theList[i] = int(word)
    for i in range(0, len(theList)):  # pulls out the first row of lines
        finalList.append(theList[i])
    return finalList


def randomizeList(input):
    # Creates a randomized list of numbers
    randomNumbers = random.sample(range(0, len(input)), len(input))
    # Takes each number and places the corresponding piece from the letter set into a list
    list = []
    for i in randomNumbers:
        list.append(input[i])
    return list


def createFile(input):
    initial = getFile(input)
    randomized = randomizeList(initial)
    primeNumberDict = {}
    number = 1
    while number < len(input):
        key = number
        value = randomized[number]
        dict = {key: value}
        primeNumberDict.update(dict)
        number += 1
    f = open("primeNumbers.py", "w")
    f.write('primeNumbers = ' + str(primeNumberDict))
    f.close()


createFile('PrimeNumberList.txt')
