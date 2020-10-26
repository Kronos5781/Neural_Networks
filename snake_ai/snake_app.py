from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import snake

# Constants
SQUARE_SIZE = (20, 20)
BOARD_SIZE = (20, 20)


# The Widget in which the Snake Game will be running
class SnakeWidget(QWidget):
    def __init__(self, board_size, square_size):
        super().__init__()
        # Constants
        self.BOARD_SIZE = board_size
        self.SQUARE_SIZE = square_size

        # Widget Config and Init
        self.setWindowTitle("Snake Widget")
        self.board_size = board_size
        self.setFixedSize(self.board_size[0] * SQUARE_SIZE[0], self.BOARD_SIZE[1] * self.SQUARE_SIZE[1])
        self.new_game()

        # Set update Time and activate update Function
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

    def update(self):
        # Update The Snake and close the window if the snake is dead
        if self.snake.is_alive:
            self.snake.update()
        else:
            print("dead")
            import sys
            sys.exit(-1)

        # Repaint the Screen
        self.repaint()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter()
        painter.begin(self)

        self.draw_snake(painter)
        self.draw_apple(painter)
        painter.end()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        key_press = event.key()
        if key_press == Qt.Key_Up and self.snake.direction != 'd':
            self.snake.direction = 'u'
        elif key_press == Qt.Key_Down and self.snake.direction != 'u':
            self.snake.direction = 'd'
        elif key_press == Qt.Key_Right and self.snake.direction != 'l':
            self.snake.direction = 'r'
        elif key_press == Qt.Key_Left and self.snake.direction != 'r':
            self.snake.direction = 'l'

    def new_game(self):
        # Generate a new snake
        self.snake = snake.Snake(self.board_size, SQUARE_SIZE)

    def draw_snake(self, painter: QtGui.QPainter) -> None:
        # Init Painter
        painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
        painter.setPen(QtGui.QPen(Qt.black))
        painter.setBrush(QtGui.QBrush(Qt.red))

        for point in self.snake.snake_array:
            painter.drawRect(point[0] * SQUARE_SIZE[0],  # Upper left x-coord
                             point[1] * SQUARE_SIZE[1],  # Upper left y-coord
                             SQUARE_SIZE[0],            # Width
                             SQUARE_SIZE[1])            # Height

    def draw_apple(self, painter: QtGui.QPainter) -> None:
        # Check if there is an apple on the board
        apple_location = self.snake.apple_location
        if apple_location:
            # Init Painter
            painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
            painter.setPen(QtGui.QPen(Qt.black))
            painter.setBrush(QtGui.QBrush(Qt.green))

            painter.drawRect(apple_location[0] * SQUARE_SIZE[0],
                             apple_location[1] * SQUARE_SIZE[1],
                             SQUARE_SIZE[0],
                             SQUARE_SIZE[1])

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Giving it some kind of standard Setup depending on the OS
    screen = SnakeWidget(BOARD_SIZE, SQUARE_SIZE) # Generate new SnakeWidget Object
    screen.show()
    sys.exit(app.exec_()) # Makes sure our window shows up nicely and exits when we want to
