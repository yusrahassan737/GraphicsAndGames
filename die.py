# Name: Yusra Hassan
# Date: September 16, 2020
# Decription: Very simple simulation of rolling a die
# Purpose: Practice with random module

# Start-Up
import random
action = input("Type \"roll\" to roll the die: ")

# Ouput a random number from 1-6 however many times the user first said to
if (action == "roll"):
    times = int(input("How many times? "))
    while times > 0:
        print(random.randint(1, 6))
        times = times - 1
