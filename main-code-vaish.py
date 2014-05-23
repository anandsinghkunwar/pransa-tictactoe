import pygame, sys
from pygame.locals import *

def check_winner(matrix):
    if(matrix[0][0]==matrix[0][1]==matrix[0][2]!='s'):
        return matrix[0][0]
    elif (matrix[1][0]==matrix[1][1]==matrix[1][2]!='s'):
        return matrix[1][0]
    elif (matrix[2][0]==matrix[2][1]==matrix[2][2]!='s'):
        return matrix[2][0]
    elif (matrix[0][0]==matrix[1][0]==matrix[2][0]!='s'):
        return matrix[0][0]
    elif (matrix[0][1]==matrix[1][1]==matrix[1][2]!='s'):
        return matrix[0][1]
    elif (matrix[0][2]==matrix[1][2]==matrix[2][2]!='s'):
        return matrix[0][2]
    elif (matrix[0][0]==matrix[1][1]==matrix[2][2]!='s'):
        return matrix[0][0]
    elif (matrix[0][2]==matrix[1][1]==matrix[2][0]!='s'):
        return matrix[0][2]
    else:
        return 's'
    
matrix =10*[['s','s','s'],['s','s','s'],['s','s','s']]
bg="bg.jpg"
crimg="x.png"
oimg="o.png"

pygame.init()

BackgroundimageObject=pygame.image.load(bg).convert()
XimageObject=pygame.image.load(crimg).convert_alpha()
OimageObject=pygame.image.load(oimg).convert_alpha()
    
screen=pygame.display.set_mode((600,600),0,32)

while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type==MOUSEDOWN:
            pass

    screen.blit(background,(0,0))

    pygame.display.update()
