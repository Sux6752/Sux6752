import pygame
import random

WIDTH = 1200
HEIGHT = 600
FPS = 60
direction = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Май игра")
clock = pygame.time.Clock()
surface = pygame.Surface((125,15))
while True:
    pygame.fpsClock.tick(FPS)
    surface.fill((255, 255 ,255))

    rect = pygame.Rect((70, 200, 10, 100))
    rect.x = 500
    rect.y = 550
    surface.blit(surface, rect)
    screen.blit(surface, rect)
    pygame.display.update()
print(surface.get_width())
print(rect.width)
print(rect.x, rect.y)
input()
rect.y+=50
rect.x+=70

# def move(direction):
#     # This function moves recalculates new image coordinates
#     if direction:
#         if direction == K_UP:
#             rect.y-=5
#         elif direction == K_DOWN:
#             rect.y+=5
#         if direction == K_LEFT:
#             rect.x-=5
#         elif direction == K_RIGHT:
#             rect.x+=5
    
# while True:
# #     move(direction)
#     for event in pygame.event.get():
#         if event.type==pygame.KEYDOWN:
#             rect.y+=50
#             rect.x+=70
    