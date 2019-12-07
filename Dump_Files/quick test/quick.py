f = open("GettysburgAddress.txt", 'r')
message = f.read()
f.close()
#'''


def message(doc, key):
    print("CIS220 Class Fall 2019                                 Help 0 | About i | Menu x")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Message"))
    print("{:^80}".format("Key: " + key))
    print("")
    mtyLine = 11 - len(doc)
    for i in doc:
        print(i, end='')
    for i in range(mtyLine):
        print("")
    print("")
    print("Hit Enter to go back, or")
    sel = input("Choose an option to proceed: ")
    return sel


doc = []
count = 0
for i in range(0, len(message), 60):
    if len(doc) < count+1:
        doc.insert(count, [])
    doc[count].append("       " + message[i:i + 15] + "  " + message[i + 15:i + 30] + "  " + message[i + 30:i + 45] + "  " + message[i + 45:i + 60] + "       \n")
    if len(doc[count]) == 9:
        count += 1

for i in range(len(doc)):
    for x in doc[i]:
        print(x, end="")
    input()


# '''

'''
doc = []

doc.insert(0, ["1","2"])
doc.insert(1, ["2"])

doc[0].append("90")
print(doc)
print(len(doc[0]))
'''

