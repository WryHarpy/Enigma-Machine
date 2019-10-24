# Nick Demanche
# 22 October 2019
# CIS220 - Object Oriented Programming
# Wheel Encrypter Class

# Import the marry function to create a usable letterset from a text document
from marry import marry

# A class which takes in a few attributes and can encrypt or decrypt a message with a given inbound
# and outbound set of letters.
class Wheel:
    def __init__(self, message, wheelPosition, inbound, outbound):
        self.self = self
        self.message = message
        self.wheelPosition = wheelPosition
        self.inbound = inbound
        self.outbound = outbound

    def __encrypt__(self):
        word = self.message
        wordOut = ''  # this is the word I am going to toss out.
        for i in range(len(word)):
            count = 0
            for j in range(len(self.inbound)):
                if word[i] == self.inbound[j]:
                    count = j
            wordOut = wordOut + self.outbound[count]
        return wordOut


letterset = marry('Letterset.txt')
plugboard = marry('Plugboard.txt')
initialMessage = 'FOURSCOREANDSEVENYEARSAGO'

wheel1 = Wheel(initialMessage, 1, letterset, plugboard)
encryptedWheel1 = wheel1.__encrypt__()
print(encryptedWheel1)
