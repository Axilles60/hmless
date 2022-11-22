import pygame
from pygame.draw import *

pygame.init()
FPS=30
screen = pygame.display.set_mode((400, 400))
screen.fill((255,255,255))
circle(screen, (255, 255, 0), (200, 175),100)
circle(screen, (0, 0, 0), (200, 175),100,1)
circle(screen, (255, 0, 0), (150, 130),25)
circle(screen, (255, 0, 0), (250, 130),25)
circle(screen, (0, 0, 0), (250, 130),12)
circle(screen, (0, 0, 0), (150, 130),12)
polygon(screen, (0, 0, 0), [(120,200), (275,200),
                               (275,225),(120,225), (120,200)])
polygon(screen, (0, 0, 0), [(120,200), (275,200),
                               (275,225),(120,225), (120,200)])
polygon(screen, (0, 0, 0), [(120,90), (130,80),
                               (200,135),(190,140), (120,90)])
polygon(screen, (0, 0, 0), [(270,90), (260,80),
                               (210,135),(220,140), (270,90)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()