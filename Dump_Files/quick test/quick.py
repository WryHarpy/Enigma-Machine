f = open("GettysburgAddress.txt", 'r')
d = f.read()
f.close()


tempList = d.split("\n")


charSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz";?!.(), -—'

Set = []

for message in tempList:
    for i in message:
        if i not in Set:
            Set.append(i)
    for i in charSet:
        if i not in Set:
            Set.append(i)


print(Set)
Set = sorted(Set)
print(Set)
letterSet = ""
for i in Set:
    letterSet = letterSet + i


print(letterSet)