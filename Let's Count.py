# Name: Yusra Hassan
# Date: December 15-16, 2020
# Class: None- Personal Project
# Description: Simple program to count with the user to an input-specified number
# Purpose: Practice with AI before creating first AI game

import random

# input variables with error handling
userTurn = input("Enter \"0\" to go first or \"1\" to go second: ")
while userTurn != str(0) and userTurn != str(1):
    userTurn = input("Try again. Enter \"0\" to go first or \"1\" to go second: ")
userTurn = int(userTurn)

maxNum = input("Enter the number to count up to: ")
while not maxNum.isdigit():
    maxNum = input("Try again. Enter the number to count up to: ")
maxNum = int(maxNum)

# Other Variables
if userTurn == 1:
    userNum = 0
else:
    userNum = input("num: ")
    while not userNum.isdigit():
        userNum = input("Try again: ")
    userNum = int(userNum)
currentNum = userNum
compNum = 0

# Main counting loop
while currentNum < maxNum:
    if currentNum % 2 == userTurn: # User inputs number
        userNum = input("num: ")
        while not userNum.isdigit() or userNum != str(compNum + 1): # error handling with inputted number
            userNum = input("Try again: ")
        userNum = int(userNum)
    
    else: # Computer prints number
        compNum = userNum + 1 # computer's number should be the user's number + 1
        print(compNum)
    
    currentNum += 1
