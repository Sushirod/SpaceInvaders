from Scene import Scene
from play_scene import PlayScene
import pygame

class GameOverScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.lgame = PlayScene(app)
        self.scoref = self.lgame.getscore()
        self.title2 = app.font.render("PERDISTE :( ", True, (255,255,255))
        self.title2_rect = self.title2.get_rect()
        self.title2_rect.center = (app.width//2, app.height//2 - 20)


        self.title = app.font2.render("Tu score fue: " + str(self.scoref), True, (255,255,255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (200, app.height-300)


        self.title3 = app.font3.render("Presiona cualquier tecla para volver a jugar ", True, (255,255,255))
        self.title3_rect = self.title.get_rect()
        self.title3_rect.center = (200, app.height-200)

        super().__init__('GameOverScene')

    def start(self):
        print('Se inicia:', self.name)
        self.scoref = self.lgame.getscore()
        self.title2_rect.x = 200
        self.title2_rect.x = self.app.height-450


    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            print('Se presiono una tecla')
            self.lgame.start()
            self.app.change_scene('intro')

    def update(self):
        self.title = self.app.font.render("Tu score fue de: " + str(self.scoref), True, (255,255,255))

    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.title2, self.title2_rect)
        self.screen.blit(self.title3, self.title3_rect)

    def exit(self):
        print('Termina:', self.name)