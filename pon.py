import pygame
import sys

FPS = 360
xp=250
yp=450

pygame.init()
sc = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("параша а не игра")
pygame.display.update()
rect = pygame.draw.rect(sc, (88, 214, 141), (xp, yp, 25, 25))

while True:
    clock.tick(FPS)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    pygame.draw.rect(sc, (88, 214, 141), (xp, yp, 10, 10))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        yp = yp -1
    if keys[pygame.K_DOWN]:
        yp = yp +1
    if keys[pygame.K_LEFT]:
        xp = xp -1
    if keys[pygame.K_RIGHT]:
        xp = xp +1
    pygame.display.flip()
    pygame.display.update()