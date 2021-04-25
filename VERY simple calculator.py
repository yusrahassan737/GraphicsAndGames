# Name: Yusra Hassan
# Date: June 25, 2020
# Description: Simple calculator
# Purpose: Practice with arithmetic operations

# Variables + Functions
validOps = ["+", "-", "/", "x", "*", "^"]
def calculate(num1, operation, num2):
  if operation == "+":
    return(float(num1) + float(num2))
  elif operation == "-":
    return(float(num1) - float(num2))
  elif operation == "/":
    return(float(num1) / float(num2))
  elif operation == "x" or operation == "*":
    return(float(num1) * float(num2))
  elif operation == "^":
    return(pow(float(num1), float(num2)))

# Start
print("This program calculates some simple single operations.")
question = input("Enter your question with one space between each number or operator: ")

# Error handling for entered question
while " " not in question or len(question.split()) != 3 or question.split()[0].count(".") > 1 or not question.replace(".","").split()[0].isdigit() or question.split()[1] not in validOps or question.split()[2].count(".") > 1 or not question.replace(".","").split()[2].isdigit():
  question = input("Try again. Enter your question with one space between each number or operator: ")

# Calculate
print(calculate(question.split()[0], question.split()[1], question.split()[2]))
