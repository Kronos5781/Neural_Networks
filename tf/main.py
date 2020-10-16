import pygame
import tensorflow as tf
import numpy as np
import random
import game

from pygame.locals import *
from tensorflow import keras

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

my_game = game.SnakeGame(SCREEN_WIDTH, SCREEN_HEIGHT)

my_game.main_game_loop()


