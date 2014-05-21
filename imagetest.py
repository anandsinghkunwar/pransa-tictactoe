import pygame
screen = pygame.display.set_mode((900,900))
image = pygame.image.load('img.jpg').convert()
screen.blit(image,(0,0))
pygame.display.flip()
done=True
while done:
        for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                        done = False

