# Name: Yusra Hassan
# Date: December 6, 2020
# Class: None- Personal Project
# Description: A math quiz (based on "Simple Quiz" program) that calculates streaks of correct answers
# Purpose: Practice with calculating streaks

# import necessary module and store streak in a global variable
import random
streak = 0

# Game loop
while True:
    # Variables (changing with each loop iteration)
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    operation = random.choice(["+", "-", "x", "/"])
    if operation == "/": # do not allow division by 0# do not allow decimal quotients
        while num2 == 0 or num1 % num2 != 0:
            num1 = random.randint(-10, 10)
            num2 = random.randint(-10, 10)
    strNum1 = str(num1)
    strNum2 = str(num2)    
    
    # put brackets around any negative number and print question
    if num1 < 0:
        strNum1 = "(" + strNum1 + ")"
    if num2 < 0:
        strNum2 = "(" + strNum2 + ")"
    
    print(strNum1, operation, strNum2)
    
    # Calculate answer and save to a variable
    if operation == "+":
        rightAnswer = num1 + num2
    elif operation == "-":
        rightAnswer = num1 - num2
    elif operation == "x":
        rightAnswer = num1 * num2 
    else:
        rightAnswer = int(num1 / num2)
    
    # allow user to input an answer and check, display streak
    userAnswer = input("is: ")
    
    if userAnswer == str(rightAnswer):
        streak += 1 # add to streak
        print("You got it! You have a streak of %i." %streak)
    elif userAnswer.lower() == "quit":
        print("Your last streak was %i." %streak)
        break # stop playing
    else:
        streak = 0 # reset streak to 0 for a wrong answer
        print("The answer was actually %i. You lost you streak." %rightAnswer)


