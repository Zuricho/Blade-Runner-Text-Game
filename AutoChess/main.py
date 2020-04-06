# Platform game

import pygame as pg
import random
from pygame.locals import *
from sys import exit
from settings import *
from sprites import *


class Game:
    def __init__(self):
        # initialize game window, etx
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        

    def new(self):
        # start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        p1 = Platform(0,HEIGHT-40,WIDTH,40)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            # Keep loop running at the same and right speed
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        self.all_sprites.update()
        # chech player hits a plat form - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        
        # if player reaches top 1/4 of the screen
        if self.player.rect.top <= HEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        # Die!
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 18)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False
        
        # spawn new platforms to keep some average number
        while len(self.platforms) < 12:
            width = random.randrange(50,100)
            p = Platform(random.randrange(0,WIDTH-width),
                         random.randrange(-75,-30),
                         width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)



    def events(self):
        # game loop - events
        # Process input (events)
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.running = False
                if self.playing:
                    self.playing = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # game loop - draw
        # Draw / render
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score),22,WHITE,WIDTH/2,15)
        # after drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game start screen
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("Arrows to move, space to jump", 22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press a key to play",22,WHITE,WIDTH/2,HEIGHT*3/4)
        pg.display.flip()
        self.wait_for_key()


    def show_go_screen(self):
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press a key to play again",22,WHITE,WIDTH/2,HEIGHT*3/4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False



    def draw_text(self,text,size,color,x,y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)


g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
