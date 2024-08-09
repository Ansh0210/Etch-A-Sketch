from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_counter():
    tim.left(10)

    # alternate way to do the same thing (angela's way)
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)


def turn_clock():
    tim.right(10)

    # alternate way to do the same thing (angela's way)
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)


def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_counter)
screen.onkey(key="d", fun=turn_clock)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
