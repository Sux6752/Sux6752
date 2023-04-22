import pygame
import random

WIDTH = 1200
HEIGHT = 600
FPS = 60
direction = 0
x = 550
y = 550

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Май игра")
clock = pygame.time.Clock()
surface = pygame.Surface((125,15))
color = (255, 255, 255)

while True:
    pygame.display.flip()
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 150, 20))
    # gets a single event from the event queue 
    event = pygame.event.wait() 
    # if the 'close' button of the window is pressed 
    if event.type == pygame.QUIT: 
        # stops the application 
        break 
    # Detects the 'KEYDOWN' and 'KEYUP' events 
    if event.type in(pygame.KEYDOWN, pygame.KEYUP): 
        # gets the key name 
        key_name = pygame.key.name(event.key) 
        # converts to uppercase the key name 
        key_name = key_name.upper() 
        # if any key is pressed 
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT):
                x+=5
            # prints on the console the key pressed 
            #print(u'"{}" key pressed'.format(key_name)) 
        # if any key is released 
        elif event.type == pygame.KEYUP: 
            # prints on the console the released key 
            print(u'"{}" key released'.format(key_name))
        clock.tick(FPS)
        pygame.display.update()