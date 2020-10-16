import pygame
from pygame.locals import *
import snake

class SnakeGame:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
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
        self.CELL_SIZE = 20
        self.update_snake = 0
        self.food = [0, 0]
        self.new_food = True
        self.new_piece = [0, 0]
        self.game_over = False
        self.clicked = False
        self.score = 0
        self.run = False

        # define colors
        self.BG_COL1 = (255, 200, 150)
        self.BG_COL2 = (255, 200, 100)
        self.BODY_INNER_COL = (50, 175, 25)
        self.BODY_OUTER_COL = (100, 100, 200)
        self.FOOD_COL = (200, 50, 50)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)

        # Init Snake
        self.my_snake = snake.Snake(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 2, self.CELL_SIZE)

    def is_game_over(self):
        if self.my_snake.snake_parts[0][0] < 0 or self.my_snake.snake_parts[0][0] > self.SCREEN_WIDTH or self.my_snake.snake_parts[0][1] < 0 or self.my_snake.snake_parts[0][1] > self.SCREEN_HEIGHT:
            self.game_over = True

    def draw_screen(self):
        # Draw Background Color
        for i in range(0, self.SCREEN_WIDTH, 2 * self.CELL_SIZE):
            for j in range(0, self.SCREEN_HEIGHT, 2 *self.CELL_SIZE):
                pygame.draw.rect(self.screen, self.BG_COL1, (j, i, self.CELL_SIZE, self.CELL_SIZE))
            for j in range(self.CELL_SIZE, self.SCREEN_HEIGHT, 2 *self.CELL_SIZE):
                pygame.draw.rect(self.screen, self.BG_COL2, (j, i, self.CELL_SIZE, self.CELL_SIZE))

            for j in range(self.CELL_SIZE, self.SCREEN_HEIGHT, 2 * self.CELL_SIZE):
                pygame.draw.rect(self.screen, self.BG_COL1, (j ,i + self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
            for j in range(0, self.SCREEN_HEIGHT, 2 * self.CELL_SIZE):
                pygame.draw.rect(self.screen, self.BG_COL2, (j, i + self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))



        # Draw FPS
        self.screen.blit(self.update_fps(), (550, 0))

        # Draw Score
        self.draw_score()


    def draw_snake(self):
        head = 1
        for x in self.my_snake.get_parts():
            if head == 0:
                pygame.draw.rect(self.screen, self.BODY_OUTER_COL, (x[0], x[1], self.CELL_SIZE, self.CELL_SIZE))
                pygame.draw.rect(self.screen, self.BODY_INNER_COL, (x[0] + 1, x[1] + 1, self.CELL_SIZE - 2, self.CELL_SIZE - 2))
            if head == 1:
                pygame.draw.rect(self.screen, self.BODY_OUTER_COL, (x[0], x[1], self.CELL_SIZE, self.CELL_SIZE))
                pygame.draw.rect(self.screen, (255, 0, 0), (x[0] + 1, x[1] + 1, self.CELL_SIZE - 2, self.CELL_SIZE - 2))
                head = 0


    def draw_score(self):
        score_txt = 'Score: ' + str(self.score)
        score_img = self.font.render(score_txt, True, self.BLUE)
        self.screen.blit(score_img, (0, 0))

    def update_fps(self):
        fps = str(int(self.clock.get_fps()))
        fps_text = self.font.render(fps, 1, pygame.Color("blue"))
        return fps_text

    def main_game_loop(self):
        self.run = True

        while self.run:

            # Call diverse Functions which update the Game State
            self.my_snake.update()
            self.draw_screen()
            self.draw_snake()


            for event in pygame.event.get():
                # Quit Game if X Button is pressed
                if event.type == pygame.QUIT:
                    self.run = False
                # Change direction according to arrow keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.my_snake.direction != 3:
                        self.my_snake.direction = 1
                    if event.key == pygame.K_RIGHT and self.my_snake.direction != 4:
                        self.my_snake.direction = 2
                    if event.key == pygame.K_DOWN and self.my_snake.direction != 1:
                        self.my_snake.direction = 3
                    if event.key == pygame.K_LEFT and self.my_snake.direction != 2:
                        self.my_snake.direction = 4

            # Update Display and set FPS
            self.clock.tick(1)
            pygame.display.update()

            self.is_game_over()
            if self.game_over:
                self.run = False
                print("moos")