import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''
    Создает новый шарик одного из шести цветов случайно где-то на экране
    x - положение центра шарика по иксу
    y - положение центра шарика по игреку
    r - радиус шарика
    '''
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    '''
    принимает создание шарика как событие
    предназначена для обнаружения положения центра шарика и его радиуса
    x - положение центра шарика по иксу
    y - положение центра шарика по игреку
    r - радиус шарика
    '''
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            print('Click!')
            if((((event.pos[0]-x)**2+(event.pos[1]-y)**2)**0.5)<=r):
                print('Ok')
    new_ball()
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()