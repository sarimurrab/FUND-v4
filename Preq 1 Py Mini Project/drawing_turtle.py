import turtle

def draw_sqaure(racer):
    for _ in range(5):
        racer.forward(200)
        racer.right(90)


def draw_turtle():
    window = turtle.Screen()
    window.bgcolor("white")

    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.speed(18)
    racer.color("green")

    for _ in range(144):
        draw_sqaure(racer)
        racer.right(5)

    window.exitonclick()


draw_turtle()
