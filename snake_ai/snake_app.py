from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
import sys
import snake

# Constants
SQUARE_SIZE = (10, 10)


# The Widget in which the Snake Game will be running
class SnakeWidget(QWidget):
    def __init__(self, board_size=(50,50)):
        super().__init__()

        # Widget Config and Init
        self.setWindowTitle("Snake Widget")
        self.board_size = board_size
        self.setFixedSize(self.board_size[0] * SQUARE_SIZE[0], self.board_size[1] * SQUARE_SIZE[1])
        self.new_game()

        # Set update Time and activate update Function
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

    def update(self):
        pass

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        pass

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        pass

    def new_game(self):
        # Generate a new snake
        self.snake = snake.Snake(self.board_size, SQUARE_SIZE)




if __name__ == "__main__":
    app = QApplication(sys.argv)  # Giving it some kind of standard Setup depending on the OS
    screen = SnakeWidget()
    screen.show()
    sys.exit(app.exec_()) # Makes sure our window shows up nicely and exits when we want to
