import pygame

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

    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        tam = self.x
        if self.move_left and self.rect.x  > 0:
            self.x -= self.speed
        if self.move_right and self.tam:
            self.x += self.speed 
        if self.x >= self.maxscreen:
            self.x = self.maxscreen

        self.rect.x = self.x
