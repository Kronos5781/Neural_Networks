import pygame
from pygame.locals import *

class Snake:

    def __init__(self, start_x, start_y, direction, cz):
        self.snake_parts = [[start_x, start_y]]
        self.snake_parts.append([start_x - cz, start_y])
        self.snake_parts.append([start_x - 2 * cz, start_y])
        self.snake_parts.append([start_x - 3 * cz, start_y])
        self.direction = direction
        self.CELL_SIZE = cz

    def update(self):
        self.snake_parts = self.snake_parts[-1:] + self.snake_parts[:-1]
        # now update the position of the head based on direction
        # heading up
        if self.direction == 1:
            self.snake_parts[0][0] = self.snake_parts[1][0]
            self.snake_parts[0][1] = self.snake_parts[1][1] - self.CELL_SIZE
        # heading down
        if self.direction == 3:
            self.snake_parts[0][0] = self.snake_parts[1][0]
            self.snake_parts[0][1] = self.snake_parts[1][1] + self.CELL_SIZE
        # heading right
        if self.direction == 2:
            self.snake_parts[0][1] = self.snake_parts[1][1]
            self.snake_parts[0][0] = self.snake_parts[1][0] + self.CELL_SIZE
        # heading left
        if self.direction == 4:
            self.snake_parts[0][1] = self.snake_parts[1][1]
            self.snake_parts[0][0] = self.snake_parts[1][0] - self.CELL_SIZE

    def get_parts(self):
        return self.snake_parts