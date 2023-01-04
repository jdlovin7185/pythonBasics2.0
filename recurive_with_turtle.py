import turtle

my_turtle = turtle.Turtle()
second_turtle = turtle.Turtle()
my_win = turtle.Screen()
my_win.setup(600, 600)


def draw_spiral(slow_poke, line_len):
    if line_len <= 0:
        return
    else:
        slow_poke.forward(line_len)
        slow_poke.left(120)
        draw_spiral(slow_poke, line_len - 10)


def draw_backward_spiral(slow_poke, line_len):
    if line_len <= 0:
        return
    else:
        slow_poke.backward(line_len)
        slow_poke.right(120)
        draw_spiral(slow_poke, line_len - 10)


draw_backward_spiral(second_turtle, 200)
draw_spiral(my_turtle, 200)
