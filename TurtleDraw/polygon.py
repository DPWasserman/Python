import turtle

painter = turtle.Turtle()

sides = 8
angle = 360/sides

for _ in range(sides):
    painter.forward(100)
    painter.left(angle)

turtle.done()