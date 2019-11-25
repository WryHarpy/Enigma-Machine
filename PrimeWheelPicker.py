import WheelDictionary, primeNumbers
#importing the wheels and prime numbers
def primePicker(index):
    Pointer=(primeNumbers.primeNumbers.get(index))
    while Pointer > 100:
        Pointer = Pointer - 100
        continue
    wheel = str(Pointer)
    temp = (WheelDictionary.Wheels.get('w'+wheel))
    return temp    
#Function that takes input for index in the prime number list and takes remainder
def wheelPicker():
     print('Enter first prime number list index')
     index1 = int(input(''))
     print('Enter second prime number list index')
     index2 = int(input(''))
     print('Enter third prime number list index')
     index3 = int(input(''))
     w1 = primePicker(index1)
     w2 = primePicker(index2)
     w3 = primePicker(index3)
     return w1, w2, w3
#Driver
wheelPicker()
