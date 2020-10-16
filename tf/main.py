import pygame
import tensorflow as tf
import numpy as np
import random
import game

from pygame.locals import *
from tensorflow import keras

# Config
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
CELL_SIZE = 20

my_game = game.SnakeGame(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
my_game.main_game_loop()


