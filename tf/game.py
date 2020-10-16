import pygame
from pygame.locals import *
import snake
import hud
import food

class SnakeGame:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE):
        # Init Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # set display name
        pygame.display.set_caption('Snakerino')

        # define font
        self.font = pygame.font.SysFont(None, 40)

        # define game variables
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.CELL_SIZE = CELL_SIZE
        self.game_over = False
        self.run = False

        # define colors
        self.BG_COL1 = (255, 255, 255)
        self.BG_COL2 = (230, 230, 255)

        # Init Objects
        self.my_snake = snake.Snake(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 2, self.CELL_SIZE)
        self.my_hud = hud.Hud(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.my_food = food.Food(400, 300, self.CELL_SIZE, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)


    def is_game_over(self):

        # Check if snake hits a wall
        if self.my_snake.snake_parts[0][0] < 0 or self.my_snake.snake_parts[0][0] > self.SCREEN_WIDTH - self.CELL_SIZE or self.my_snake.snake_parts[0][1] < 0 or self.my_snake.snake_parts[0][1] > self.SCREEN_HEIGHT - self.CELL_SIZE:
            self.game_over = True

        # Check if snake bites itself
        head_count = 0
        for x in self.my_snake.get_parts():
            if self.my_snake.get_parts()[0] == x and head_count > 0:
                self.game_over = True
            head_count += 1

    def get_input(self):
        for event in pygame.event.get():
            # Quit Game if X Button is pressed
            if event.type == pygame.QUIT:
                self.run = False
            # Change direction according to arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.my_snake.get_direction() != 3:
                    self.my_snake.set_direction(1)
                if event.key == pygame.K_RIGHT and self.my_snake.get_direction() != 4:
                    self.my_snake.set_direction(2)
                if event.key == pygame.K_DOWN and self.my_snake.get_direction() != 1:
                    self.my_snake.set_direction(3)
                if event.key == pygame.K_LEFT and self.my_snake.get_direction() != 2:
                    self.my_snake.set_direction(4)

    def draw(self):
        # Draw Background Grid
        for i in range(0, self.SCREEN_HEIGHT, 2 * self.CELL_SIZE):
            for j in range(0, self.SCREEN_WIDTH, 2 *self.CELL_SIZE):
                pygame.draw.rect(self.screen, self.BG_COL1, (j, i, self.CELL_SIZE, self.CELL_SIZE))
            for j in range(self.CELL_SIZE, self.SCREEN_WIDTH, 2 *self.CELL_SIZE):
                pygame.draw.rect(self.screen, self.BG_COL2, (j, i, self.CELL_SIZE, self.CELL_SIZE))

            for j in range(self.CELL_SIZE, self.SCREEN_WIDTH, 2 * self.CELL_SIZE):
                pygame.draw.rect(self.screen, self.BG_COL1, (j ,i + self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
            for j in range(0, self.SCREEN_WIDTH, 2 * self.CELL_SIZE):
                pygame.draw.rect(self.screen, self.BG_COL2, (j, i + self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))

    def main_game_loop(self):
        self.run = True

        while self.run:

            # Get the input from Keyboard and Mouse
            self.get_input()

            # Call diverse Functions which update the Game Status
            self.draw()
            self.my_snake.update(self.screen, self.my_food.get_food_pos())
            self.my_food.update(self.screen, self.my_snake.get_new_food())
            self.my_hud.update(self.screen, self.clock)

            self.my_hud.set_score(self.my_snake.get_food_eaten())


            # Test if the Game is Over
            self.is_game_over()

            # If game_over is true stop the game
            if self.game_over:
                self.run = False

            # Update Display and set FPS
            self.clock.tick(15)
            pygame.display.update()