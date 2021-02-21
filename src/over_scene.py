from Scene import Scene
import pygame

class GameOverScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.title = app.font.render("PERDISTE", True, (255,255,255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (app.width//2, app.height//2)
        super().__init__('GameOverScene')

    def start(self):
        print('Se inicia:', self.name)

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            print('Se presiono una tecla')
            self.app.change_scene('intro')

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.title, self.title_rect)

    def exit(self):
        print('Termina:', self.name)