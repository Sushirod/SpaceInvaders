import pygame

class Bullet:
    def __init__(self, app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/disparo2.png")
        self.rect = self.image.get_rect()
        self.yspeed = 0.2
        self.active = False

    def draw(self):
        if(self.active):
            self.screen.blit(self.image, self.rect)
    
    def update(self):
        if(self.active):
            self.rect.y -= self.yspeed
