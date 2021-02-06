from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_square(position)

    def move(self):
        for square in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square - 1].xcor()
            new_y = self.squares[square - 1].ycor()
            self.squares[square].goto(new_x, new_y)
        self.squares[0].forward(20)

    def add_square(self, position):
        square = Turtle(shape='square')
        square.penup()
        square.color('white')
        square.goto(position)
        self.squares.append(square)

    def extend(self):
        self.add_square(self.squares[-1].position())

    def up(self):
        if not (self.squares[0].heading() == 270):
            self.squares[0].setheading(90)

    def down(self):
        if not (self.squares[0].heading() == 90):
            self.squares[0].setheading(270)

    def right(self):
        if not (self.squares[0].heading() == 180):
            self.squares[0].setheading(0)

    def left(self):
        if not (self.squares[0].heading() == 0):
            self.squares[0].setheading(180)

    def reset(self):
        for snake in self.squares:
            snake.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

