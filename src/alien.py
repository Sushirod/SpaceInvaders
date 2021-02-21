import pygame

class Alien:
    def __init__(self,app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/alienfinal.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self.speed = 0.1
        self.yspeed = 0.001
        self.maxscreen = self.screen_rect.width - 140
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        self.x += self.speed
        self.y += self.yspeed

        if(self.x > self.maxscreen):
            self.speed *= -1
        if(self.x < 0):
            self.speed *= -1
        
        self.rect.x = self.x
        self.rect.y = self.y
