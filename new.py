import pygame
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ultimate Tic-Tac-Toe")

#op until the user clicks the close button.
done = True
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
pygame.draw.rect(screen, RED, [55,50,100,50])
pygame.display.flip()
pygame.draw.rect(screen, GREEN, [100,100,100,100])
pygame.display.flip()
# -------- Main Program Loop -----------
while done:
# ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get(): # User did something
		print event
		if event.type == pygame.QUIT: # If user clicked close
			done = False 
	clock.tick(20) # put a space before this

