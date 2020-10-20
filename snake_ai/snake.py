class Snake:
    def __init__(self, board_size, square_size):
        # Constants
        self.BOARD_SIZE = board_size
        self.SQUARE_SIZE = square_size

        # Vars
        self.score = 0
        self.direction = ''
        self.velocity = [0, 0]
        self.pos = (self.BOARD_SIZE[0] // 2, self.BOARD_SIZE[1] // 2)
        self.apple_location = None
        self.is_alive = False

        #Start Game
        self.init_snake('r')
        self.init_vel('r', (1, 0))
        self.generate_apple()

    def init_snake(self, starting_direction):
        """
        Initializing the snake
            starting_direction --> The direction the snake should start facing, which ever direction it is, the head of
            the snake will start facing this way.
        """
        head = [self.pos[0], self.pos[1]]
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
            snake = [head, [head[0] - 2, head[1]], [head[0] - 2, head[1]]]

        # Copy the Generated Snake into the snake_array and set it alive
        self.snake_array = snake
        self.is_alive = True


    def init_vel(self, starting_direction, initial_velocity):
        self.velocity = initial_velocity

    def update(self):
        pass

    def is_dead(self):
        pass

    def generate_apple(self):
        pass
