# Name: Yusra Hassan
# Date: November 15, 2020
# Description: Figure out how to work alpha values for colour tuples, create a gradient

# Start-up
import pygame
pygame.init()
SIZE = (400, 400)
screen = pygame.display.set_mode(SIZE)

# Variables
running = True

# Draw
pygame.draw.rect(screen, (255, 255, 0, 255), (150, 100, 50, 50))
rect = pygame.Rect(0, 150, 50, 50)
otherScreen = pygame.Surface(SIZE, pygame.SRCALPHA)
for i in range(51):
    pygame.draw.rect(otherScreen, (255, 0, 255, i * 5 + 5), (i * 10, 150, 10, 50))

screen.blit(otherScreen, rect)


# End-off
while running:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
