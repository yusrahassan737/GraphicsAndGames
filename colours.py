# Name: Yusra Hassan
# Date: October 3, 2020
# Description: Helps user choose a colour and creates a centered circle in pygame, with it.

hue = input("Choose a hue. (Red, orange, yellow, green, blue or purple) ")
while (hue.lower() != "red" and hue.lower() != "orange" and hue.lower() != "yellow" and hue.lower() != "green" and hue.lower() != "blue" and hue.lower() != "purple"):
    print("You haven't entered a valid hue.")
    hue = input("Choose a hue. (Red, orange, yellow, green, blue or purple) ")

brightness = input("Light or dark? ")
while (brightness.lower() != "light" and brightness.lower() != "dark"):
    print("You haven't entered a valid response.")
    brightness = input("Light or dark? ")

screenSize = int(input("The screen will be a square. Enter a screen size: "))

import pygame
pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize))

red = [(214, 82, 75), (138, 16, 10)]
orange = [(235, 188, 138), (237, 131, 19)]
yellow = [(237, 216, 130), (227, 186, 20)]
green = [(164, 235, 148), (39, 148, 15)]
blue = [(114, 191, 207), (39, 83, 138)]
purple = [(163, 147, 173), (106, 15, 122)]

if (hue.lower() == "red"):
    if (brightness.lower() == "light"):
        colour = red[0]
    else:
        colour = red[1]
elif (hue.lower() == "orange"):
    if (brightness.lower() == "light"):
        colour = orange[0]
    else:
        colour = orange[1]
elif (hue.lower() == "yellow"):
    if (brightness.lower() == "light"):
        colour = yellow[0]
    else:
        colour = yellow[1]
elif (hue.lower() == "green"):
    if (brightness.lower() == "light"):
        colour = green[0]
    else:
        colour = green[1]
elif (hue.lower() == "blue"):
    if (brightness.lower() == "light"):
        colour = blue[0]
    else:
        colour = blue[1]
elif (hue.lower() == "purple"):
    if (brightness.lower() == "light"):
        colour = purple[0]
    else:
        colour = purple[1]

pygame.draw.circle(screen, colour, (screenSize // 2, screenSize // 2), screenSize // 4)

pygame.display.flip()
pygame.time.wait(1000)

pygame.quit()