import os
import pygame
import sys

pygame.init()

FPS = 60    # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'SOURCE', 'cat.png'))
catImg = pygame.image.load(catPath)
catx = 10
caty = 10
direction = 'right'
catVel = 3


def quit():
    pygame.quit()
    sys.exit()


while True:  # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += catVel
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += catVel
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= catVel
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= catVel
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()

    pygame.display.update()
    fpsClock.tick(FPS)
