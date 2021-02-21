from Scene import Scene
import pygame

class IntroScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.title = app.font.render("SPACE INVADERS", True, (255,255,255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (app.width//2, app.height//2)

        self.title2 = app.font2.render("Usa las flechas y la tecla espacio!!", True, (255,255,255))
        self.title2_rect = self.title.get_rect()
        self.title2_rect.center = (400, app.height-250)


        self.title3 = app.font3.render("Presiona cualquier tecla para jugar ", True, (255,255,255))
        self.title3_rect = self.title.get_rect()
        self.title3_rect.center = (370, app.height-200)

        super().__init__('IntroScene')

    def start(self):
        print('Se inicia:', self.name)

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.app.change_scene('play')

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.title2, self.title2_rect)
        self.screen.blit(self.title3, self.title3_rect)


    def exit(self):
        print('Termina:', self.name)