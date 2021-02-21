import pygame
from bullet import Bullet

class Ship:
    def __init__(self,app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.maxscreen = self.screen_rect.width - 40
        self.speed = 0.3
        self.x = float(self.rect.x)
        self.move_right = False
        self.move_left = False
        self.tam = self.x
        self.bulletlist = []
        self.number_bullets = 10
        self.shooting = False
        self.last_fire = pygame.time.get_ticks()
        self.cooldown = 200

    def start(self):
        self.charge()

    def draw(self):
        self.screen.blit(self.image, self.rect)
        for bullet in self.bulletlist:
            bullet.draw()
    
    def update(self):
        if self.move_left and self.rect.x  > 0:
            self.x -= self.speed
        if self.move_right and self.tam:
            self.x += self.speed 
        if self.x >= self.maxscreen:
            self.x = self.maxscreen

        self.rect.x = self.x

        for bullet in self.bulletlist:
            bullet.update()

        for bullet in self.bulletlist:
            if(bullet.rect.y < 1):
                bullet.active = False
                bullet.draw()

        if(self.shooting):
            self.shoot(self.x + 15, self.rect.y-10)
    
    def charge(self):
        for i in range(self.number_bullets):
            bullet = Bullet(self)
            self.bulletlist.append(bullet)
    
    def shoot(self, x , y):
        now = pygame.time.get_ticks()
        if(now - self.last_fire >= self.cooldown):
            self.last_fire = now
            for bullet in self.bulletlist:
                if(bullet.active == False):
                    bullet.rect.x = x
                    bullet.rect.y = y
                    bullet.active = True
                    return