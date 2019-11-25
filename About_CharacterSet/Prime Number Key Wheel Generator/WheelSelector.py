# Nick Demanche
# 24 November 2019
# CIS220 - Object Oriented Programming
# Takes in Prime Number list and Wheel List to get a keyed selection of the wheel
# that will be used for encryption

from primeNumbers import primeNumbers
from WheelDictionary import Wheels

def wheelSelector(numOfWheels):
    selection = input('Select what key you would like to use: ')
    keyValue = primeNumbers.get(int(selection)) # Takes the key and gets the associated prime number
    wheelnumber = keyValue % int(numOfWheels) # Divides the prime number by 5(the # of Wheels) and gets the remainder
    wheel = 'w' + str(wheelnumber) # creates the key name of the wheel you selected
    selectedWheel = Wheels.get(wheel) # Gets the associated randomized letter set
    return selectedWheel

decision = wheelSelector(5)

print(decision)