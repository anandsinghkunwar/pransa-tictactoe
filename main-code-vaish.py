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
    elif (matrix[0][1]==matrix[1][1]==matrix[2][1]!='s'):
        return matrix[0][1]
    elif (matrix[0][2]==matrix[1][2]==matrix[2][2]!='s'):
        return matrix[0][2]
    elif (matrix[0][0]==matrix[1][1]==matrix[2][2]!='s'):
        return matrix[0][0]
    elif (matrix[0][2]==matrix[1][1]==matrix[2][0]!='s'):
        return matrix[0][2]
    else:
        return 's'
    
matrix=[[[['s','s','s'],['s','s','s'],['s','s','s']] for x in xrange(3)] for x in xrange(3)]
main_matrix=[['s','s','s'],['s','s','s'],['s','s','s']]

coord_of_cells = [[[[[0 for x in xrange(2)] for x in xrange(3)] for x in xrange(3)] for x in xrange(3)] for x in xrange(3)]

for x in xrange(3):
    for y in xrange(3):
        for i in xrange(3):
            for j in xrange(3):
                coord_of_cells[x][y][i][j]=(210*y+70*j,210*x+70*i)
                
bg="./img/grid.png"
xsimg="./img/xsmall.png"
osimg="./img/osmall.png"
xlimg="./img/xbig.png"
olimg="./img/obig.png"

pygame.init()
    
screen=pygame.display.set_mode((630,630),0,32)

BackgroundimageObject=pygame.image.load(bg).convert()
XSMALLimageObject=pygame.image.load(xsimg).convert_alpha()
OSMALLimageObject=pygame.image.load(osimg).convert_alpha()
XLARGEimageObject=pygame.image.load(xlimg).convert_alpha()
OLARGEimageObject=pygame.image.load(olimg).convert_alpha()

player=1
iprev=-1
jprev=-1

screen.blit(BackgroundimageObject,(0,0))

while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type==MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            for x in xrange(3):
                for y in xrange(3):
                    for i in xrange(3):
                        for j in xrange(3):
                            if ((pos[0]>coord_of_cells[x][y][i][j][0])and(pos[0]<coord_of_cells[x][y][i][j][0]+70)and(pos[1]>coord_of_cells[x][y][i][j][1])and(pos[1]<coord_of_cells[x][y][i][j][1]+70)):

                                if (matrix[x][y][i][j]!='s'):
                                    pass

                                elif((iprev==-1)and(jprev==-1)):
                                    if(player%2==1):
                                        screen.blit(XSMALLimageObject,coord_of_cells[x][y][i][j])
                                        player+=1
                                        matrix[x][y][i][j]='x'
                                        iprev=i
                                        jprev=j

                                    else:
                                        screen.blit(OSMALLimageObject,coord_of_cells[x][y][i][j])
                                        player+=1
                                        matrix[x][y][i][j]='o'
                                        iprev=i
                                        jprev=j
                                
                                elif((x==iprev)and(y==jprev)):
                                    if(player%2==1):
                                        screen.blit(XSMALLimageObject,coord_of_cells[x][y][i][j])
                                        player+=1
                                        matrix[x][y][i][j]='x'
                                        iprev=i
                                        jprev=j
                                        
                                    else:
                                        screen.blit(OSMALLimageObject,coord_of_cells[x][y][i][j])
                                        player+=1
                                        matrix[x][y][i][j]='o'
                                        iprev=i
                                        jprev=j

                                else:
                                    pass

                                if(check_winner(matrix[x][y])!='s'):
                                    if(check_winner(matrix[x][y])=='x'):
                                        screen.blit(XLARGEimageObject,coord_of_cells[x][y][0][0])
                                        main_matrix[x][y]='x'

                                    else:
                                        screen.blit(OLARGEimageObject,coord_of_cells[x][y][0][0])
                                        main_matrix[x][y]='o'

                                    if(check_winner(main_matrix)!='s'):
                                        print "The winner is "+ check_winner(main_matrix)
                                        pygame.quit()
                                        sys.exit()

                                if(main_matrix[iprev][jprev]!='s'):
                                    iprev=-1
                                    jprev=-1
                                

    pygame.display.update()
