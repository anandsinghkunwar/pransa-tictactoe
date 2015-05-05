import pygame, sys
from pygame.locals import *
from subprocess import call
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

def deletecontent(filename):					# To clear data files on exit for cleanliness
	with open(filename, "w"):
		pass

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
psmall="./img/presentsmall.png"
pbig="./img/presentbig.png"
pygame.init()
    
screen=pygame.display.set_mode((630,630),0,32)

BackgroundimageObject=pygame.image.load(bg).convert()
XSMALLimageObject=pygame.image.load(xsimg).convert_alpha()
OSMALLimageObject=pygame.image.load(osimg).convert_alpha()
XLARGEimageObject=pygame.image.load(xlimg).convert_alpha()
OLARGEimageObject=pygame.image.load(olimg).convert_alpha()
TLARGEimageObject=pygame.image.load(timg).convert_alpha()
PRESENTSMALLimageObject=pygame.image.load(psmall).convert_alpha()
PRESENTLARGEimageObject=pygame.image.load(pbig).convert_alpha()

player=1
iprev=-1
jprev=-1
class Board(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self,img):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       self.image = img
       self.rect = self.image.get_rect()

board = Board(BackgroundimageObject)
board.rect= [0,0]
all_sprite_list = pygame.sprite.OrderedUpdates()

all_sprite_list.add(board)
all_sprite_list.draw(screen)
pygame.display.flip()
call(["gcc","./src/monte_carlo.c","-o","./playmonte"])		#Compiles the program for different systems
highg=0
highlight = Board(PRESENTLARGEimageObject)
highlight.rect= [0,0]
all_sprite_list.add(highlight)
all_sprite_list.draw(screen)
highg=highlight
pygame.display.flip()


while True:

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
	    deletecontent("./data/aimove.txt")
	    deletecontent("./data/matrixforai.txt")
            sys.exit()
        
        if event.type==MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            for x in xrange(3):
                for y in xrange(3):
                    for i in xrange(3):
                        for j in xrange(3):
                            if ((pos[0]>coord_of_cells[x][y][i][j][0])and(pos[0]<coord_of_cells[x][y][i][j][0]+70)and(pos[1]>coord_of_cells[x][y][i][j][1])and(pos[1]<coord_of_cells[x][y][i][j][1]+70)):

                                if (matrix[x][y][i][j]!='s'):
                                    continue

                                elif((iprev==-1)and(jprev==-1)):
                                    if(main_matrix[x][y]=='s'):
                                        if(player%2==1):
                                            
                                            board = Board(XSMALLimageObject)
                                            board.rect= coord_of_cells[x][y][i][j]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
					    player+=1
                                            matrix[x][y][i][j]='x'
                                            iprev=i
                                            jprev=j

                                        else:
                                            board = Board(OSMALLimageObject)
                                            board.rect= coord_of_cells[x][y][i][j]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            player+=1
                                            matrix[x][y][i][j]='o'
                                            iprev=i
                                            jprev=j
                                    else:
                                        continue
                                elif((x==iprev)and(y==jprev)):
                                    if(player%2==1):
                                        board = Board(XSMALLimageObject)
                                        board.rect= coord_of_cells[x][y][i][j]
                                        
                                        all_sprite_list.add(board)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()
                                        player+=1
                                        matrix[x][y][i][j]='x'
                                        iprev=i
                                        jprev=j
                                        
                                    else:
                                        board = Board(OSMALLimageObject)
                                        board.rect= coord_of_cells[x][y][i][j]
                                        
                                        all_sprite_list.add(board)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()
                                        player+=1
                                        matrix[x][y][i][j]='o'
                                        iprev=i
                                        jprev=j

                                else:
                                    continue

                                if(check_winner(matrix[x][y])!='s'):
                                    if(check_winner(matrix[x][y])=='x'):
                                        board = Board(XLARGEimageObject)
                                        board.rect= coord_of_cells[x][y][0][0]
                                        all_sprite_list.add(board)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()
                                        main_matrix[x][y]='x'

                                    elif(check_winner(matrix[x][y])=='o'):
                                        board = Board(OLARGEimageObject)
                                        board.rect= coord_of_cells[x][y][0][0]
                                        all_sprite_list.add(board)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()
                                        main_matrix[x][y]='o'

                                    else:
                                        board = Board(TLARGEimageObject)
                                        board.rect= coord_of_cells[x][y][0][0] 
                                        all_sprite_list.add(board)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()
                                        main_matrix[x][y]='t'

                                    if(check_win_main(main_matrix)!='s'):

                                        if(check_win_main(main_matrix)!='t'):
                                            print "The winner is "+ check_win_main(main_matrix)
                                        else:
                                            print "The game is a tie"

                                        pygame.quit()
					deletecontent("./data/aimove.txt")
					deletecontent("./data/matrixforai.txt")
                                        sys.exit()

                                if(main_matrix[iprev][jprev]!='s'):
                                    iprev=-1
                                    jprev=-1

                                #Finished one move
                                all_sprite_list.remove(highlight)
                                pygame.display.flip()
                                fout=open("./data/matrixforai.txt","w")
                                fout.write(str(iprev)+" "+str(jprev)+"\n")

                                for var1 in range(3):
                                    for var2 in range(3):
                                        for var3 in range(3):
                                            for var4 in range(3):
                                                if(matrix[var1][var3][var2][var4]=='s'):
                                                    fout.write("-")
                                                elif(matrix[var1][var3][var2][var4]=='x'):
                                                    fout.write("X")
                                                elif(matrix[var1][var3][var2][var4]=='o'):
                                                    fout.write("O")
                                        fout.write("\n")
                                fout.write("\n")            #Is this required??
                                fout.close()

                                pygame.display.update() # Required?

                                print "Please wait"                 #Debugging
                                call(["./playmonte"])

                                fin=open("./data/aimove.txt","r")

                                a=fin.read()

                                print a
                                a=a.split()

                                fin.close()

                                var1=int(a[0])
                                var2=int(a[1])
                                var3=int(a[2])
                                var4=int(a[3])

                                board = Board(OSMALLimageObject)
                                board.rect= coord_of_cells[var1][var2][var3][var4]
                                
                                all_sprite_list.add(board)
                                all_sprite_list.draw(screen)
                                pygame.display.flip()
                                player+=1
                                matrix[var1][var2][var3][var4]='o'
                                iprev=var3
                                jprev=var4

                                if(check_winner(matrix[var1][var2])!='s'):
                                    if(check_winner(matrix[var1][var2])=='o'):
                                        board = Board(OLARGEimageObject)
                                        board.rect= coord_of_cells[var1][var2][0][0]
                                        
                                        all_sprite_list.add(board)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()
                                        main_matrix[var1][var2]='o'

                                    else:
                                        board = Board(TLARGEimageObject)
                                        board.rect= coord_of_cells[var1][var2][0][0]
                                        all_sprite_list.add(board)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()
                                        main_matrix[var1][var2]='t'

                                    if(check_win_main(main_matrix)!='s'):

                                        if(check_win_main(main_matrix)!='t'):
                                            print "The winner is "+ check_win_main(main_matrix)
                                        else:
                                            print "The game is a tie"
					
                                        pygame.quit()
					deletecontent("./data/aimove.txt")
					deletecontent("./data/matrixforai.txt")
                                        sys.exit()

                                if(main_matrix[iprev][jprev]!='s'):
                                    iprev=-1
                                    jprev=-1
                                
                                if ((iprev==-1)and(jprev==-1)):
                                    highlight = Board(PRESENTLARGEimageObject)
                                    highg = highlight
                                    highlight.rect= [0,0]
                                    all_sprite_list.add(highlight)
                                    all_sprite_list.draw(screen)
                                    pygame.display.flip()
                                else:
                                    highlight = Board(PRESENTSMALLimageObject)
                                    highg = highlight
                                    highlight.rect= coord_of_cells[iprev][jprev][0][0]
                                    all_sprite_list.add(highlight)
                                    all_sprite_list.draw(screen)
                                    pygame.display.flip()

                                
                                #Code added here only

