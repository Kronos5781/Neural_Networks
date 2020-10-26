from typing import Tuple, Optional, Union
import random
from collections import deque
import sys

class Snake:
    def __init__(self, board_size, square_size):
        # Constants
        self.BOARD_SIZE = board_size
        self.SQUARE_SIZE = square_size

        # Vars
        self.score = 0
        self.direction = ''
        self.starting_pos = (self.BOARD_SIZE[0] // 2, self.BOARD_SIZE[1] // 2)
        self.apple_location = None
        self.is_alive = False

        #Start Game
        self.init_snake('r')
        self.generate_apple()

    def init_snake(self, starting_direction):
        """
        Initializing the snake
            starting_direction --> The direction the snake should start facing, which ever direction it is, the head of
            the snake will start facing this way.
        """
        global snake
        head = self.starting_pos

        if starting_direction == 'u':
            snake = [head, (head[0], head[1] + 1), (head[0], head[1] + 2)]
        # Body is above
        elif starting_direction == 'd':
            snake = [head, (head[0], head[1] - 1), (head[0], head[1] - 2)]
        # Body is to the right
        elif starting_direction == 'l':
            snake = [head, (head[0] + 1, head[1]), (head[0] + 2, head[1])]
        # Body is to the left
        elif starting_direction == 'r':
            snake = [head, [head[0] - 1, head[1]], [head[0] - 2, head[1]]]

        # Copy the Generated Snake into the snake_array copy the starting direction and set it alive
        self.snake_array = deque(snake)
        self.direction = starting_direction
        self.is_alive = True

    def update(self) -> bool:
        global next_pos

        # Is snake even alive
        if not self.is_alive:
            return False

        # Is the direction valid?
        direction = self.direction
        if direction not in ('u', 'd', 'l', 'r'):
            return False

        head = self.snake_array[0]
        # Move the Head
        if self.direction == 'u':
            next_pos = (head[0], head[1] - 1)
        elif self.direction == 'd':
            next_pos = (head[0], head[1] + 1)
        elif self.direction == 'r':
            next_pos = (head[0] + 1, head[1])
        elif self.direction == 'l':
            next_pos = (head[0] - 1, head[1])

        # Is the next position we want to move to valid?
        if self._is_valid(next_pos):
            self.snake_array.appendleft(next_pos)
            # If we just consumed the apple, generate a new one.
            # No need to pop the tail of the snake since the snake is growing here
            if next_pos == self.apple_location:
                self.generate_apple()
                self.score += 1
            else:
                self.snake_array.pop()

            return True
        else:
            self.is_alive = False
            return False

    def is_dead(self):
        pass

    def generate_apple(self):
        width = self.BOARD_SIZE[0]
        height = self.BOARD_SIZE[1]

        # Find all possibilities for a apple to be placed
        possibilities = [divmod(i, height) for i in range(width * height) if divmod(i, height) not in self.snake_array]

        # if there are any possibilities left place an apple at a random location
        if possibilities:
            self.apple_location = possibilities[random.randint(0, len(possibilities))]
        else:
            # I guess you win?
            print('you won!')
            pass

    def _is_valid(self, next_pos) -> bool:
        """
        Determine whether a given position is valid.
        Return True if the position is on the board and does not intersect the snake.
        Return False otherwise
        """
        if (next_pos[0] < 0) or (next_pos[0] > self.BOARD_SIZE[0] - 1):
            return False
        if (next_pos[1] < 0) or (next_pos[1] > self.BOARD_SIZE[1] - 1):
            return False

        for pos in self.snake_array:
            if pos == self.snake_array[-1]:
                continue
            elif pos == next_pos:
                return False

        return True