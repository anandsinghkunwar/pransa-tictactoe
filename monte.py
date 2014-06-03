import pygame, sys
from pygame.locals import *
import time
import random

def check_win_main(matrix):

    copy_matrix_x=[['s' for x in xrange(3)] for x in xrange(3)]
    copy_matrix_o=[['s' for x in xrange(3)] for x in xrange(3)]
    
    for x in xrange(3):
        for y in xrange(3):
            if(matrix[x][y]=='t'):
                copy_matrix_x[x][y]='s'
            else:
                copy_matrix_x[x][y]=matrix[x][y]

    for x in xrange(3):
        for y in xrange(3):
            if(matrix[x][y]=='t'):
                copy_matrix_o[x][y]='s'
            else:
                copy_matrix_o[x][y]=matrix[x][y]

#    if((check_winner(copy_matrix_o)=='o') and (check_winner(copy_matrix_x)=='x')):
#        return 's'

    if(check_winner(copy_matrix_o)=='o'):
        return 'o'

    elif(check_winner(copy_matrix_x)=='x'):
        return 'x'
    
    elif(True):
        flag=0

        for x in xrange(3):
            for y in xrange(3):
                if(matrix[x][y]=='s'):
                    flag=1
                    break;

        if(flag==0):
            return 't'

    return 's'
    

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
        for x in xrange(3):
            for y in xrange(3):
                if(matrix[x][y]=='s'):
                    return 's'
    return 't'

#Monte Carlo

def random_moves(matrix,main_matrix,firstmove):

   # print firstmove

    matrix[firstmove[0]][firstmove[1]][firstmove[2]][firstmove[3]]='o'
    
    if(check_winner(matrix[firstmove[0]][firstmove[1]])=='o'):
        main_matrix[firstmove[0]][firstmove[1]]='o'
        if(check_win_main(main_matrix)=='o'):
        #    print 'fo'
            return 'o'

    if(main_matrix[firstmove[2]][firstmove[3]]!='s'):
        iplay=-1
        jplay=-1

    else:
        iplay=firstmove[2]
        jplay=firstmove[3]

#Dividing between the first move and loop.

    while(True):
        if(iplay==-1 and jplay==-1):
            iplay=random.randint(0,2)
            jplay=random.randint(0,2)
            while(main_matrix[iplay][jplay]!='s'):
                iplay=random.randint(0,2)
                jplay=random.randint(0,2)
        #        print '$'
                
        xrand=random.randint(0,2)
        yrand=random.randint(0,2)
        while(matrix[iplay][jplay][xrand][yrand]!='s'):
            xrand=random.randint(0,2)
            yrand=random.randint(0,2)
         #   print '%'

       # print 'xplay'
      #  print [iplay,jplay,xrand,yrand]                 #debugging

        matrix[iplay][jplay][xrand][yrand]='x'

        if(check_winner(matrix[iplay][jplay])=='x'):
            main_matrix[iplay][jplay]='x'
            if(check_win_main(main_matrix)=='x'):
         #       print 'x'                               #debuggging
                return 'x'

            elif(check_win_main(main_matrix)=='t'):
        #        print 't'                           #debuggging
                return 't'

        elif(check_winner(matrix[iplay][jplay])=='t'):
            main_matrix[iplay][jplay]='t'
            if(check_win_main(main_matrix)=='t'):
       #         print 't'                           #debuggging
                return 't'

        if(main_matrix[xrand][yrand]!='s'):
            iplay=-1
            jplay=-1

        else:
            iplay=xrand
            jplay=yrand

# Dividing line between first and second move

        if(iplay==-1 and jplay==-1):
            iplay=random.randint(0,2)
            jplay=random.randint(0,2)
            while(main_matrix[iplay][jplay]!='s'):
                iplay=random.randint(0,2)
                jplay=random.randint(0,2)
         #       print '$'
                
        xrand=random.randint(0,2)
        yrand=random.randint(0,2)
        while(matrix[iplay][jplay][xrand][yrand]!='s'):
            xrand=random.randint(0,2)
            yrand=random.randint(0,2)
        #    print '%'

                
    #    print 'oplay'
     #   print [iplay,jplay,xrand,yrand]             #debuggoing 

        matrix[iplay][jplay][xrand][yrand]='o'

        if(check_winner(matrix[iplay][jplay])=='o'):
            main_matrix[iplay][jplay]='o'
            if(check_win_main(main_matrix)=='o'):
  #              print 'o'                           #debuggging
                return 'o'

            elif(check_win_main(main_matrix)=='t'):
 #               print 't'                           #debuggging
                return 't'

        elif(check_winner(matrix[iplay][jplay])=='t'):
            main_matrix[iplay][jplay]='t'
            if(check_win_main(main_matrix)=='t'):
#                print 't'                           #debuggging
                return 't'
            

        if(main_matrix[xrand][yrand]!='s'):
            iplay=-1
            jplay=-1

        else:
            iplay=xrand
            jplay=yrand


def monte_carlo(matrix,main_matrix,iplay,jplay):
    positions=[]

    if (iplay!=-1 and jplay!=-1):
        for i in range(3):
            for j in range(3):
                 if (matrix[iplay][jplay][i][j]=='s'):
                     positions.append([iplay,jplay,i,j])

    else:
        for i in range(3):
            for j in range(3):
                if (main_matrix[i][j]=='s'):                    # I think I need to pass the parameter where this data is already stored instead of checking again.
                    for x in range(3):
                        for y in range(3):
                            if (matrix[i][j][x][y]=='s'):
                                positions.append([i,j,x,y])

    best_prob=0.0
    bestpos=[-1,-1,-1,-1]
    
    for currpos in positions:
#        print currpos
        timepermove=1.0/len(positions)                      #currently at 1 second.
        
        noofwins=0
        nooflosses=0
        noofties=0

        cp_matrix=[[[['s','s','s'],['s','s','s'],['s','s','s']] for temp in xrange(3)] for temp in xrange(3)]
        cp_main_matrix=[['s','s','s'],['s','s','s'],['s','s','s']]

        init_time=time.time()
        while (time.time()-init_time<timepermove):

            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        for d in range(3):
                            cp_matrix[a][b][c][d]=matrix[a][b][c][d]

            for a in range(3):
                for b in range(3):
                    cp_main_matrix[a][b]=main_matrix[a][b]
                            
            temp=random_moves(cp_matrix,cp_main_matrix,currpos)

            if (temp=='o'):                                     #AI has been assumed to be playing second i.e.:'o'
                noofwins+=1

            elif (temp=='x'):
                nooflosses+=1

            else:
                noofties+=1

        print noofwins
        print nooflosses
        print noofties
        prob=(noofwins)*1.0/(noofwins+nooflosses+noofties)

        print noofwins+nooflosses+noofties                      #For improving the code. Trying to see how many times it can run.
        print prob
        
        if (prob>best_prob):
            best_prob=prob
            bestpos=currpos
            

    return bestpos                                               #Again I am not sure about call_by_reference and call_by_pos


#Monte Carlo

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
timg="./img/tie.png"

pygame.init()
    
screen=pygame.display.set_mode((630,630),0,32)

BackgroundimageObject=pygame.image.load(bg).convert()
XSMALLimageObject=pygame.image.load(xsimg).convert_alpha()
OSMALLimageObject=pygame.image.load(osimg).convert_alpha()
XLARGEimageObject=pygame.image.load(xlimg).convert_alpha()
OLARGEimageObject=pygame.image.load(olimg).convert_alpha()
TLARGEimageObject=pygame.image.load(timg).convert_alpha()

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
                                    if(main_matrix[x][y]=='s'):
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

                                    elif(check_winner(matrix[x][y])=='o'):
                                        screen.blit(OLARGEimageObject,coord_of_cells[x][y][0][0])
                                        main_matrix[x][y]='o'

                                    else:
                                        screen.blit(TLARGEimageObject,coord_of_cells[x][y][0][0])
                                        main_matrix[x][y]='t'

                                    if(check_win_main(main_matrix)!='s'):

                                        if(check_win_main(main_matrix)!='t'):
                                            print "The winner is "+ check_win_main(main_matrix)
                                        else:
                                            print "The game is a tie"

                                        pygame.quit()
                                        sys.exit()

                                if(main_matrix[iprev][jprev]!='s'):
                                    iprev=-1
                                    jprev=-1

                                if(player>20):
                                    print monte_carlo(matrix,main_matrix,iprev,jprev)
                                

    pygame.display.update()
