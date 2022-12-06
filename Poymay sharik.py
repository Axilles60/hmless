from random import randint

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
font_name = pygame.font.match_font('arial')

count = 9
score = 0
x = [0] * count
y = [0] * count
r = [0] * count
sp_x = [0] * count
sp_y = [0] * count
color = [0] * count


def draw_text(surf, text, size, x, y):
    '''
    :param surf: поверхность, на которой будет выводиться текст
    :param text: то, что будет выводиться в виде текста
    :param size: размер шрифта
    :param x: положение по x надписи
    :param y: положение по y надписи
    '''
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def new_ball():
    '''
    Создает новый шарик со случайной скоростью одного из шести цветов случайно где-то на экране
    x - положение центра шарика по иксу
    y - положение центра шарика по игреку
    r - радиус шарика
    sp_x - скорость по x шариков
    sp_y - скорость по y шариков
    color - цвет шариков
    '''
    global x, y, r, sp_x, sp_y, color
    for i in range(count):
        x[i] = randint(100, 700)
        y[i] = randint(100, 500)
        r[i] = randint(30, 50)
        sp_x[i] = randint(1, 20)
        sp_y[i] = randint(1, 20)
        color[i] = COLORS[randint(0, 5)]
        circle(screen, color[i], (x[i], y[i]), r[i])


def click(event):
    '''
    предназначена для обновления счетчика, если игрок попадает по шарику
    x - положение центра шарика по иксу
    y - положение центра шарика по игреку
    r - радиус шарика
    score - колво попаданий
    '''
    global x, y, r, score
    for i in range(count):
        if ((((event.pos[0] - x[i]) ** 2 + (event.pos[1] - y[i]) ** 2) ** 0.5) <= r[i]):
            score += 1
            for j in range(count):
                sp_x[i] = sp_x[i] + 2
                sp_y[i] = sp_y[i] + 2


def dvizh():
    global x, y, r, sp_x, sp_y, color
    for i in range(count):
        x[i] = x[i] + sp_x[i]
        y[i] = y[i] + sp_y[i]
        if (x[i] < 0 or x[i] > 1000):
            sp_x[i] = -sp_x[i]
            color[i] = COLORS[randint(0, 5)]
        if (y[i] < 0 or y[i] > 800):
            sp_y[i] = -sp_y[i]
            color[i] = COLORS[randint(0, 5)]
    screen.fill(BLACK)
    for i in range(count):
        circle(screen, color[i], (x[i], y[i]), r[i])


new_ball()
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
    dvizh()
    draw_text(screen, str(score), 40, 20, 10)
    pygame.display.update()

pygame.quit()
