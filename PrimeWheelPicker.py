import evWheels
#importing the wheels
arr = [] 
with open("scrambledPrimeNumbers.txt") as file:
    for line in file: 
         line = int(line)
         arr.append(line) 
#Setting up the array, could just as easily import another dictionary
def primePicker(index):
    Pointer=(arr[index])
    while Pointer > 50:
        Pointer = Pointer - 50
        continue
    wheel = str(Pointer)
    print (evWheels.Wheels.get('w'+wheel))
#Function that takes input for index in the prime number list and takes remainder
print('Enter first prime number list index')
index1 = int(input(''))
print('Enter second prime number list index')
index2 = int(input(''))
print('Enter third prime number list index')
index3 = int(input(''))
primePicker(index1)
primePicker(index2)
primePicker(index3)
#Driver
