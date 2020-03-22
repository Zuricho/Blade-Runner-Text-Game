import pygame
from pygame.locals import *
from sys import exit


SCREEN_SIZE = (640, 480)
FPS = 30

# Define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# Game loop
running = True
while running:
    # Keep loop running at the same and right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()
    
    # Draw / render
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()


