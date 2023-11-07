import turtle
import time
import math

FRAME_SIZE = 480
SQUARE_SIZE = 24
SHIFTED_SQUARE_SIZE = math.sqrt(2) * SQUARE_SIZE


def square(color: str, square_length: float = 24.0):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(square_length)
        turtle.lt(90)
    turtle.end_fill()


def shift_square(color: str = "orange", square_length: float = SHIFTED_SQUARE_SIZE, angle=45):
    turtle.lt(angle)
    square(color, square_length)
    turtle.lt(-angle)


def move_by(x_axis: int = SQUARE_SIZE, y_axis: int = SQUARE_SIZE):
    turtle.pu()
    turtle.fd(x_axis)
    turtle.lt(90)
    turtle.fd(y_axis)
    turtle.pd()
    turtle.lt(-90)


def frame(num_of_tiles: int, color: str):
    for _ in range(4):
        for _ in range(num_of_tiles):
            square(color)
            turtle.pu()
            turtle.fd(SQUARE_SIZE)
            turtle.pd()
        turtle.lt(90)


def small_piece():
    for _ in range(3):
        shift_square("orange")
        move_by()
    move_by(-SQUARE_SIZE, -SQUARE_SIZE * 3)
    shift_square("red")
    move_by()
    shift_square("red")
    move_by(SQUARE_SIZE, -SQUARE_SIZE)
    shift_square("red")


def big_piece():
    for _ in range(4):
        small_piece()
        move_by(3 * SQUARE_SIZE)
        turtle.lt(90)


def full_inside():
    for _ in range(4):
        big_piece()
        move_by(15 * SQUARE_SIZE)
        turtle.lt(90)


def draw_lawn():
    move_by(-FRAME_SIZE // 2, -FRAME_SIZE // 2)
    square("green", FRAME_SIZE)
    frame(FRAME_SIZE // SQUARE_SIZE, "green")
    move_by()
    frame(FRAME_SIZE // SQUARE_SIZE - 2, "orange")
    move_by(2 * SQUARE_SIZE)
    full_inside()


turtle.tracer(2)
draw_lawn()
time.sleep(4)
