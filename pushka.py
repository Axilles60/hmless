import math
import random
from random import choice

import pygame
from pygame.draw import *

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
font_name = pygame.font.match_font('arial')
WIDTH = 800
HEIGHT = 600
gravity = 2
score = 0


def draw_text(surf, text, size, x, y):
    '''
    Рисует текст

    :param surf: поверхность, на которой будет выводиться текст
    :param text: то, что будет выводиться в виде текста
    :param size: размер шрифта
    :param x: положение по x надписи
    :param y: положение по y надписи
    '''
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
            x - начальное положение мяча по горизонтали
            y - начальное положение мяча по вертикали

        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = random.randint(10, 20)
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self, grav):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x - self.r < 0 or self.x + self.r > WIDTH:
            self.vx = -self.vx
        if self.y - self.r < 0 or self.y + self.r > HEIGHT:
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy
        self.vy -= grav

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        global score
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= (self.r + obj.r) ** 2:
            score += 1
            return True

        return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 2
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 20
        self.y = 450

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global bullet
        bullet += 1
        new_ball = Ball(self.screen)
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        '''
        рисует ствол пушки
        '''
        stvol = 10 + self.f2_power * 1.2
        sinan = math.sin(self.an)
        cosan = math.cos(self.an)
        line(screen, self.color, (self.x, self.y), (self.x + stvol * cosan, self.y + stvol * sinan), 7)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 60:
                self.f2_power += 0.5
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.r = random.randint(10, 50)
        self.color = choice(GAME_COLORS)
        self.x = random.randint(self.r, WIDTH - self.r)
        self.y = random.randint(self.r, HEIGHT - self.r)
        self.vx = random.randint(5, 30)
        self.vy = random.randint(5, 30)
        self.live = 1
        self.new_target()

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if (self.x - self.r < 0 or self.x + self.r > WIDTH):
            self.vx = -self.vx
        if (self.y - self.r < 0 or self.y + self.r > HEIGHT):
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy

    def new_target(self):
        """ Инициализация новой цели. """
        r = self.r = random.randint(10, 50)
        x = self.x = random.randint(self.r, WIDTH - self.r)
        y = self.y = random.randint(self.r, HEIGHT - self.r)
        self.color = choice(GAME_COLORS)
        self.live = 1

    def draw(self):
        circle(self.screen, self.color, (self.x, self.y), self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
target = []
clock = pygame.time.Clock()
gun = Gun(screen)
for i in range(3):
    new_target = Target(screen)
    target.append(new_target)
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    for i in target:
        i.move()
    for b in balls:
        '''
        a=random.randint(0,3)
        if a==0:
            b.move(gravity)
        elif a==1:
            b.move(gravity-0.5)
            b.move(gravity+0.5)
        elif a==2:
            b.move(gravity-0.3)
            b.move(gravity+0.3)
            b.move(gravity+1)
        '''
        for i in target:
            if b.hittest(i) and i.live:
                i.live = 0
                i.new_target()
    gun.power_up()

    screen.fill(WHITE)
    gun.draw()
    for i in target:
        i.draw()
    for b in balls:
        b.draw()
    draw_text(screen, str(score), 40, 40, 10)
    pygame.display.update()

pygame.quit()
