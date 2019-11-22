'''
    Program :  ScreenBuilder.py
    Author  :  Ed Cauthorn
    Date    :  Sept 27, 2019
    Synopsis:  This takes a file, workfile.txt and makes it into a python moduel.

'''

from datetime import date
import os

def getFile():
    finalList =[]
    fO = open('workFile.txt', 'r')
    theList = fO.readlines()
    fO.close()
    for i in range(len(theList)):
        word = ''
        tl= theList[i]
        for k in range(1,len(tl)):  # removes the vertical line Number 
            word = word + tl[k]
        word = word.replace('\n','')
        theList[i] = word
    for i in range(1, len(theList)):    # pulls out the first row of lines
        finalList.append(theList[i])
    return finalList

    
def buildHeader(name, aut, date, synop):
    name = 'Program: ' + name + '\n'
    aut = 'Author : ' + aut + '\n'
    date = 'Date   : ' + date + '\n'
    synop = 'Synopis: ' + synop + '\n'
    line = "'''\n" + name + aut + date + synop + "'''\n"
    return line



a = 'Welcome to Screen Builder\n\n'
b = 'Please fill-out the following'
q1 = 'Program Name:  ' 
q2 = 'Author      :  '
q3 = 'Date        :  '
q4 = 'Synopsis    :  '
q5 = 'def Name    :  '


testList = getFile()

print(a + b)

pgmName = eval('input(q1) + ".py"')     # You don't have to add .py for the name
pgmAuth = "Quang Hoang"     #input(q2) You can change it to your name
pgmDate = str(date.today())     #input(q3) Automate the date
pgmSynop = input(q4)
defName = input(q5)

print("\nScreen module created.")
print("Location: {}".format(os.getcwd()))   # This shows where is the program being created


line = buildHeader(pgmName, pgmAuth, pgmDate, pgmSynop)
defName = 'def ' + defName + '():\n'
for i in range ((len(testList)-1)):
    testList[i] = '    print("' + testList[i] + '")\n'
   
testList[23] = '    sel = input("Select a number to proceed: ' + testList[23] + '")'
fO = open(pgmName, 'w')
fO.write(line)
fO.write(defName) 
for i in range (len(testList)):
    fO.write(testList[i])
fO.write('\n    return sel') 
fO.close()



