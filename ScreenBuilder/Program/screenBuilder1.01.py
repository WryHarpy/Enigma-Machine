'''
    Program: ScreenBuilder.py
    Authors : Ed Cauthorn & John Hayes
    Date   : Oct 04, 2019
    Synopsis:
    This takes a file, workfile.txt and makes it into a python moduel.

'''

'''
This part grabs the workFile template. 
I might change this in the future to not need one.
'''
def getFile():
    finalList =[]
    fO = open('workFile.txt', 'r')
    theList = fO.readlines()
    fO.close()
    for i in range(len(theList)):
        word = ''
        tl= theList[i]
        for k in range(1,len(tl)): # removes the line Number 
            word = word + tl[k]
        word = word.replace('\n','')
        theList[i] = word
    for i in range(1, len(theList)):  # pulls out the first row of lines
        finalList.append(theList[i])
    return finalList
'''
This part builds the header.
'''    
def buildHeader(name, aut, date, synop):
    name = 'Program: ' + name + '\n'
    aut = 'Author : ' + aut + '\n'
    date = 'Date    : ' + date + '\n'
    synop = 'Synopis: ' + synop + '\n'
    line = "'''\n" + name + aut + date + synop + "'''\n"
    return line

'''
These are the strings that are called in the questions. 
I have added one more for the input line.
'''

contQ = "'''"
a = 'You are in the ScreenBuilder.py.\n'
b = 'Answer the following Questions.\n'
c = 'Hit any key to proceed\n' 
q1 = 'What is the Name of the Program? ' 
q2 = 'Who is the Author? '
q3 = 'Enter todays Date? '
q4 = 'Enter what you want as a Synopsis? '
q5 = 'Enter what do you want to call the def?'
q6 = 'Enter what would you like your input line to ask?'

testList=getFile()

'''
This next section has the user input the questions at the start.
I've added a new part for creating the input line question.
'''

line = a + b + c
input(line) 
pgmName = input(q1)+'.py'
pgmAuth = input(q2)
pgmDate = input(q3)
pgmSynop = input(q4)
defName = input(q5) 
defName2 = defName
inputquestion = input(q6)

'''
This next part builds the innards that are displayed. 
I have edited it to display the input line that we type in the questions.
'''

line = buildHeader(pgmName, pgmAuth, pgmDate, pgmSynop)
defName = 'def ' + defName + '():\n'
for i in range ((len(testList)-1)):
    testList[i] = '    print("' + testList[i] + '")\n'   
testList[23] = '    sel = input("' + testList[23] + inputquestion +'")'
fO = open(pgmName, 'w')
fO.write(line)
fO.write(defName) 
for i in range (len(testList)):
    fO.write(testList[i])
fO.write('\n    return sel') 

'''
This bottom part creates the call for making the screen and 
the input part that allows the screen to stay displayed in command line.
'''

fO.write('\n'+ defName2 + '()')
fO.write('\ninput()')
fO.close()
