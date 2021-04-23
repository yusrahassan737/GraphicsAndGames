# This program will simulate rolling a die
import random

a = input("Type \"roll\" to roll the die: ")

if (a == "roll"):
    b = int(input("How many times? "))
    while b > 0:
        print(random.randint(1, 6))
        b = b - 1
