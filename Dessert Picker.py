# Name: Yusra Hassan
# Date: (Initially Created) June 19, 2020
# Description: Takes input and outputs a dessert and its properties
# Purpose: Fun, basic python practice (especially input and error handling)

# Variables and instructions
validClrs = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "mauve", "scarlet", "turquoise", "teal", "violet", "brown", "beige", "maroon", "periwinkle"]
desserts = ("cupcakes", "macaroons", "macarons", "cookies", "icecream cakes","meringues", "donuts", "brownies", "truffles", "pies")
print("In this program, fill in some info and I will find you the dessert you deserve (and how many).")

# Get name
print("\nWhat is your name?")
name = input("Enter name: ").capitalize()
if name.lower() == "shiza":
    print("Hello weirdo.")
elif name.lower() == "yusra":
    print("Hello cool person.")
else:
    print("Hello " + name + ".")

# Get colour
print("\nWhat is your favourite colour?")
favColour = input("Enter colour: ")
while favColour.lower() not in validClrs:
    print("\n" + favColour + " is not a valid colour. You can do better " + name + ".")
    favColour = input("Enter colour: ")
print("Cool.")

# Get age
print("\nWhat is your age?")
age = input("Enter age: ")
while not age.isdigit() or int(age) < 0:
  age = input("Enter a valid age: ")
print("Wow, you're old!")

# Get a random number
print("\nFinally, tell me a number from one to ten.")
num = input("Enter number: ")
while not num.isdigit() or int(num) < 1 or int(num) > 10:
  num = input("Enter a valid age: ")
print("Thanks!")

# Print the answer
print("\n" + name + ", your deserved desserts are " + age + " " + favColour + " " + desserts[int(num) - 1] + "!")
