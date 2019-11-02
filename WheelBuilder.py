# Nick Demanche
# 22 October 2019
# CIS220 - Object Oriented Programming
# Wheel Builder

import random
letterSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -,."
letterSetList = list(letterSet)
letterSetDict = { i : letterSetList[i] for i in range(0, len(letterSetList))}

# Takes in the original letterset and randomizes it then returns that as a string
def randomizeList(input):
    # Creates a randomized list of numbers
    randomNumbers = random.sample(range(0, len(input)), len(input))
    # Takes each number and places the corresponding piece from the letter set into a list
    list = []
    for i in randomNumbers:
        list.append(input[i])
    # Turns the list into a simple string of the new randomized letter set
    string = ''
    for i in list:
        string += i
    return string

# Given the amount of wheels you want and the letter set, creates
# a dictionary containing each wheel as a key:value Pair
def wheelBuilder(amount, input):
    wheelDict = {}
    number = 1
    # For each wheel, runs randomizeList and adds that to the full dictionary
    while number <= amount:
        key = 'w{}'.format(number)
        value = randomizeList(input)
        dict = {key: value}
        wheelDict.update(dict)
        number += 1
    f = open("evWheels.py", 'w')
    f.write(str(wheelDict))
    f.close()
    return wheelDict


wheelBuilder(50, letterSetDict)
