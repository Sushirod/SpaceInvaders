import pygame

class Score:
    def __init__(self,app):
        self.app = app
        self.screen = app.screen
        self.score = 0
        self.title = self.app.font2.render("Score: " + str(self.score), True, (0,0,0))
        self.title_rect = self.title.get_rect()
    
    def update(self):
        self.title = self.app.font2.render("Score: " + str(self.score), True, (0,0,0))