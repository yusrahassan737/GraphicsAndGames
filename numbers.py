#Tells smallest and largest number from randomized set

import random

myList = []

for counter in range(50):
    i = random.randint(1,1000)
    myList.append(i)

print(myList)

smallest = 1000
largest = 0
for n in myList:
    if (n > largest):
        largest = n
    if (n < smallest):
        smallest = n
print("The smallest number is", smallest)
print("The largest number is", largest)
