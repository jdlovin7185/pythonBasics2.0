import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
my_win.setup(500, 500)


def draw_spiral(slow_poke, line_len):
    if line_len <= 0:
        return
    else:
        slow_poke.forward(line_len)
        slow_poke.left(90)
        draw_spiral(slow_poke, line_len - 10)


draw_spiral(my_turtle, 150)
