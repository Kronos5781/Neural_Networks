from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
import sys
from typing import List
from snake import *

SQUARE_SIZE = (8, 8)

class SnakeWidget(QtWidgets.QWidget):
    def __init__(self, board_size=(50, 50)):
        super().__init__()
        self.board_size = board_size
        self.setFixedSize(SQUARE_SIZE[0] * self.board_size[0], SQUARE_SIZE[1] * self.board_size[1])
        self.new_game()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000./15)
        self.show()

    def new_game(self) -> None:
        self.snake = Snake(self.board_size, seed=0)

    def update(self):
        self.repaint()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = SnakeWidget()
    sys.exit(app.exec_())