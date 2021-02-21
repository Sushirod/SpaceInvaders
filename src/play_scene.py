from Scene import Scene
from ship import Ship
from alien import Alien
import pygame
import asyncio
import time

class PlayScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.ship = Ship(app)
        self.alienslist = []
        self.direccion = "izq"
        self.touchwall = False
        super().__init__('PlayScene')

    def start(self):
        print('Se inicia:', self.name)
        self.aliens()
        self.ship.start()

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

        for alien in self.alienslist:
            alien.update(self.direccion, self.touchwall)
            if(alien.x < 0):
                self.direccion = "der"
                for alien in self.alienslist:
                    alien.yspeed += 0.006
            elif(alien.x > self.app.width- 30):
                self.direccion = "izq"
                for alien in self.alienslist:
                    alien.yspeed += 0.006

            if(alien.y > self.app.height-80):
                self.app.change_scene('over')
                self.__init__(self.app)
                self.start()

    def draw(self):
        self.screen.fill((255,255,255))
        self.ship.draw()
        for alien in self.alienslist:
            alien.draw()

    def exit(self):
        print('Termina:', self.name)

    def aliens(self):
        for i in range(50, self.app.width-50, 80):
            for j in range(50, 200, 50):
                self.alien = Alien(self, i, j)
                self.alienslist.append(self.alien)
    