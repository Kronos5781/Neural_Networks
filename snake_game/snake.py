import pygame
from pygame.locals import *

class Snake:

    def __init__(self, start_x, start_y, direction, cz):
        self.snake_parts = [[start_x, start_y]]
        self.snake_parts.append([start_x - cz, start_y])
        self.snake_parts.append([start_x - 2 * cz, start_y])
        self.snake_parts.append([start_x - 3 * cz, start_y])
        self.direction = direction
        self.food_eaten = 0
        self.CELL_SIZE = cz
        self.new_food = False

        # Define Colors of the Snake
        self.BODY_INNER_COL = (50, 175, 25)
        self.BODY_OUTER_COL = (100, 100, 200)

    def update(self, screen, pos_food):

        # Move the whole snake forward one tile
        self.snake_parts = self.snake_parts[-1:] + self.snake_parts[:-1]
        # Update Position of the head based of the direction
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

        # Check if Food has been eaten
        self.has_food_been_eaten(pos_food)

        # Call Draw Function
        self.draw(screen)


    def draw(self, screen):

        head = 1
        for x in self.snake_parts:
            if head == 0:
                pygame.draw.rect(screen, self.BODY_OUTER_COL, (x[0], x[1], self.CELL_SIZE, self.CELL_SIZE))
                pygame.draw.rect(screen, self.BODY_INNER_COL,
                                 (x[0] + 1, x[1] + 1, self.CELL_SIZE - 2, self.CELL_SIZE - 2))
            if head == 1:
                pygame.draw.rect(screen, self.BODY_OUTER_COL, (x[0], x[1], self.CELL_SIZE, self.CELL_SIZE))
                pygame.draw.rect(screen, (255, 0, 0), (x[0] + 1, x[1] + 1, self.CELL_SIZE - 2, self.CELL_SIZE - 2))
            head = 0

    def has_food_been_eaten(self, pos_food):
        self.new_food = False
        if self.snake_parts[1] == pos_food:
            # create a new piece at the last point of the snake's tail
            new_piece = list(self.snake_parts[-1])
            # add an extra piece to the snake
            if self.direction == 1:
                new_piece[1] += self.CELL_SIZE
            # heading down
            if self.direction == 3:
                new_piece[1] -= self.CELL_SIZE
            # heading right
            if self.direction == 2:
                new_piece[0] -= self.CELL_SIZE
            # heading left
            if self.direction == 4:
                new_piece[0] += self.CELL_SIZE

            # attach new piece to the end of the snake
            self.snake_parts.append(new_piece)

            # Increase Score
            self.food_eaten += 1

            # Mark that food is gone
            self.new_food = True


    def get_parts(self):
        return self.snake_parts

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def get_new_food(self):
        return self.new_food

    def get_food_eaten(self):
        return self.food_eaten