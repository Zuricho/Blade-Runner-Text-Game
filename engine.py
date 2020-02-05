'''
Created on Feb 5 2020
Author: Zuricho
'''

# _*_ coding: utf-8 _*_


import pygame
from pygame.locals import *

import random

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((5,5))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()


    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1,0)

        # Restrict Player in screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My First Game")
# clock = pygame.time.Clock()


player = Player()
player.rect.move_ip(400,300)


# Game main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False


    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)


    screen.fill(BLACK)

    screen.blit(player.surf,player.rect)

    # Update
    pygame.display.flip()




