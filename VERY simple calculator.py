""" Current problems : It takes 3 lines to enter a problem
It can not solve problems using more than one operation
It does not allow another "calc" after "ans"
Make a mouse-interactive pygame one?
"""

print("This program calculates some simple operations.")
action = input("Type \"calc\" to perform the operation: ")

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

while action == "calc":
  ans = calculate(input("Enter your first number: "), input("Enter an operation(+, -, x, /, ^): "), input("Enter your second number: "))
  print(ans)
  action = input("Type \"calc\" to perform another operation or \"ans\" to perform an operation on your previous answer: ")

while action == "ans":
  newAns = calculate(ans, input("Enter an operation(+, -, x, /, ^): "), input("Enter your second number: "))
  print(newAns)
  action = input("Type \"calc\" to perform another operation or \"ans\" to perform an operation on your previous answer: ")
  ans = newAns

