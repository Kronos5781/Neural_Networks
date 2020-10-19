import pygame
import numpy as np
from pygame.locals import *

class Food:

    def __init__(self, x, y, cz, sw, sh):
        self.pos = [x, y]
        self.CELL_SIZE = cz
        self.SCREEN_WIDTH = sw
        self.SCREEN_HEIGHT = sh
        self.FOOD_COL = (200, 50, 50)

    def update(self, screen, new_food):

        if new_food:
            self.pos[0] = np.random.randint(0, (self.SCREEN_WIDTH // self.CELL_SIZE) - 1) * self.CELL_SIZE
            self.pos[1] = np.random.randint(0, (self.SCREEN_HEIGHT // self.CELL_SIZE) - 1) * self.CELL_SIZE

        self.draw(screen)

    def draw(self, screen):
        pygame.draw.rect(screen, self.FOOD_COL, (self.pos[0], self.pos[1], self.CELL_SIZE, self.CELL_SIZE))

    def get_food_pos(self):
        return self.pos