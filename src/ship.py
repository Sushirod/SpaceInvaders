import pygame

class Ship:
    def __init__(self,app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = 0.15
        self.x = float(self.rect.x)
        self.move_right = False
        self.move_left = False
        self.border = self.rect.x + self.rect.width - 10

    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.move_left and self.border < self.screen_rect.width:
            self.x -= self.speed
        if self.move_right and self.border > 0:
            self.x += self.speed
        self.rect.x = self.x
