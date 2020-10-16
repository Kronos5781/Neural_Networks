import pygame
from pygame.locals import *


class Hud:

    def __init__(self, sw, sh):
        self.score = 0
        self.SCREEN_WIDTH = sw
        self.SCREEN_HEIGHT = sh
        self.font = pygame.font.SysFont(None, 40)
        self.TEXT_COL = (0, 0, 0)

    def update(self, screen, clock):
        self.draw(screen, clock)

    def draw(self, screen, clock):
        # Draw FPS
        screen.blit(self.update_fps(clock), (self.SCREEN_WIDTH - 50, 0))

        # Draw Score
        score_txt = 'Score: ' + str(self.score)
        score_img = self.font.render(score_txt, True, self.TEXT_COL)
        screen.blit(score_img, (0, 0))

    def update_fps(self, clock):
        # Get the current FPS
        fps = str(int(clock.get_fps()))
        fps_text = self.font.render(fps, 1, pygame.Color(self.TEXT_COL))
        return fps_text

    def set_score(self, score):
        self.score = score