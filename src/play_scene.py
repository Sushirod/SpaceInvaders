from Scene import Scene
from ship import Ship
from alien import Alien
import pygame
import asyncio
import time

score = 0

class PlayScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.image = pygame.image.load("assets/images/fondofinal.jpg")
        self.rect = self.image.get_rect()
        self.lscore = score
        self.title = app.font2.render("Score: " + str(self.lscore), True, (0,0,0))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (app.width//2, app.height//2)
        self.ship = Ship(app)
        self.alienslist = []
        self.direccion = "izq"
        self.touchwall = False
        super().__init__('PlayScene')

    def start(self):
        print('Se inicia:', self.name)
        self.aliens()
        self.ship.start()
        self.title_rect.x = 10
        self.title_rect.y = 10
        self.lscore = 0
        global score
        score = 0

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.ship.move_left = True
            if event.key == pygame.K_RIGHT:
                self.ship.move_right = True
            if event.key == pygame.K_SPACE:
                self.ship.shooting = True  

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.ship.move_left = False
            if event.key == pygame.K_RIGHT:
                self.ship.move_right = False 
            if event.key == pygame.K_SPACE:
                self.ship.shooting = False  

    def update(self):
        self.ship.update()
        self.title = self.app.font2.render("Score: " + str(self.lscore), True, (0,0,0))
        for alien in self.alienslist:
            alien.update(self.direccion, self.touchwall)
            if(alien.x < 0):
                self.direccion = "der"
                for alien in self.alienslist:
                    alien.yspeed += 0.008
            elif(alien.x > self.app.width- 30):
                self.direccion = "izq"
                for alien in self.alienslist:
                    alien.yspeed += 0.008

            if(alien.y > self.app.height-80):
                self.app.change_scene('over')
        
        if(len(self.alienslist)<= 0):
            self.aliens()

        self.collisions()
        global score
        self.lscore = score

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.title, self.title_rect)
        self.ship.draw()
        for alien in self.alienslist:
            alien.draw()

    def exit(self):
        print('Termina:', self.name)

    def aliens(self):
        if(len(self.alienslist)>= 1):
            self.alienslist.clear()
        for i in range(50, self.app.width-50, 100):
            for j in range(50, 200, 50):
                self.alien = Alien(self, i, j)
                self.alienslist.append(self.alien)

    def collisions(self):
        for bullet in self.ship.bulletlist:
            for alien in self.alienslist:
                if bullet.active == True:
                    if(bullet.rect.x < alien.x + alien.rect.width and 
                    bullet.rect.x + bullet.rect.width > alien.rect.x and
                    bullet.rect.y < alien.rect.y + alien.rect.height and
                    bullet.rect.y + bullet.rect.height> alien.rect.y):
                        bullet.active = False
                        self.alienslist.remove(alien)
                        global score
                        score += 1
                        print(self.lscore)

    def getscore(self):
        return score
    