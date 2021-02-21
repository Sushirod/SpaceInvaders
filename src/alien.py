import pygame

class Alien:
    def __init__(self, app, x , y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/alienfinal.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0.1
        self.yspeed = 0.02
        self.maxscreen = self.screen_rect.width - 140
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self, direccion, touchwall):
        if(direccion == "der"):
            self.x += self.speed
        if (direccion == "izq"):
            self.x -= self.speed
        if(touchwall):
            self.incremento()
            print("entre")
            touchwall = False
        self.y += self.yspeed
        self.rect.x = self.x
        self.rect.y = self.y
    
    def incremento(self):
        self.yspeed += 0.1
