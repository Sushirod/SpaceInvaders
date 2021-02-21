import pygame
import asyncio
from intro_scene import  IntroScene
from play_scene import PlayScene
from over_scene import GameOverScene


class PyagemApp():
    def __init__(self):
        self.running = True
        self.fps = 60
        self.active_scene = None
        self.width = 650
        self.height = 650
        self.font = None
        self.font2 = None
        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        self.load_assets()
        self.scenes = {'intro': IntroScene(self), 'play': PlayScene(self), 'over': GameOverScene(self)}
        self.change_scene('intro')

    def change_scene(self, scene_name):
        if self.active_scene is not None: 
            self.active_scene.exit()
        self.active_scene = self.scenes[scene_name]
        self.active_scene.start()

    def load_assets(self): 
        self.font = pygame.font.Font('assets/fonts/DOSIS-SEMIBOLD.TTF', 62)
        self.font2 = pygame.font.Font('assets/fonts/DOSIS-SEMIBOLD.TTF', 20)
        self.font3 = pygame.font.Font('assets/fonts/DOSIS-SEMIBOLD.TTF', 25)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.active_scene.process_events(event)

    def update(self):
        self.active_scene.update()

    def draw(self):
        pygame.display.flip()
        self.active_scene.draw()

    def run(self):
        while self.running:
            self.process_events()
            self.update()
            self.draw()

app = PyagemApp()

app.run()

pygame.quit()