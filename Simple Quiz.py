# Name: Yusra Hassan
# Date: general idea = summer 2020; creation = Nov. 26, 2020
# Description: Asks simple math questions to the user until they get one wrong, counts correct questions
# Purpose: Simple practice with input games

# import module and store points in a global variable
import random
points = 0

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
    else: # round answer to two decimal places when necessary, for division
        rightAnswer = int(num1 / num2)
    
    # allow user to input an answer and check, display points
    userAnswer = input("is: ")
    
    if userAnswer == str(rightAnswer):
        points += 1 # add points for a correct answer
        print("You got it! You have %i point(s)." %points)
    else:
        print("The answer was actually %i. You made it to %i point(s)." %(rightAnswer, points))
        break # stop playing if for a wrong answer
