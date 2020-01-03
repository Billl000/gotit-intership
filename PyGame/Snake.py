import random, pygame, sys
from pygame.locals import *

#Variables
FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0
assert WINDOWHEIGHT % CELLSIZE == 0
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (255,   0,   0)
GREEN = (0, 255,   0)
DARKGREEN = (0, 155,   0)
DARKGRAY = (40,  40,  40)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def drawSnake():
    
def runGame():
    DISPLAYSURF.fill(BGCOLOR)


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Worm', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Wormy!', True, GREEN)

    degrees1 = 0
    degrees2 = 0
    running = True

    while running:
        DISPLAYSURF.fill(BGCOLOR)

        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

#        drawPressKeyMsg()

#        if checkForKeyPress():
        screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

        #Display Stuff
        #imageFood = pygame.image.load(".png").convert()
        #screen.blit(imageFood, (120, 120))
        imageSnake = pygame.image.load("snake.png").convert()
        xSnake = 80
        for i in range(0, 5):
            screen.blit(imageSnake, (xSnake, 80))
            x += 25

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

        pygame.display.update()
        FPSCLOCK.tick(FPS)
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Worm')

    showStartScreen()



if __name__ == '__main__':
    main()

# Hien thi screen
# Hien thi dc ran
# Hien thi do an random
# Dieu khien con ran
# An dc do an (ran dai ra, do an bien mat va tp random)
# Scores