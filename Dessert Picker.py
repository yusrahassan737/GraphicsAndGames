# Name: Yusra Hassan
# Date: (Initially Created) June 19, 2020
# Description: Takes input and outputs a dessert and its properties
# Purpose: Basic python practice (especially input)

print("In this program, fill in some info and I will find you the dessert you deserve.")
print("\n")
print("What is your name?")
name = input("Enter name: ")
if name == "shiza" or name == "Shiza":
    print("Hello weirdo.")
elif name == "Yusra" or name == "yusra":
    print("Hello cool person.")
else:
    print("Hello " + name + ".")

nopeSet = {"black", "Black", "grey", "Grey", "white", "White"}
print("\n")
print("What is your favourite colour?")
favColour = input("Enter colour: ")
while favColour in nopeSet:
    print(favColour + " is a shade -not a colour. You can do better " + name + ".")
    favColour = input("Enter colour: ")
print("Cool.")

print("\n")
print("What is your age?")
age = input("Enter age: ")

print("\n")
print("Finally, tell me a number from one to ten.")
num = input("Enter number: ")

desserts = ("cupcakes", "macaroons", "macarons", "cookies", "icecream cakes","meringues", "donuts", "brownies", "truffles", "pies")
k = int(num)- 1

print("\n")
print(name + ", your deserved desserts are " + age + " " + favColour + " " + desserts[k] + ".")
