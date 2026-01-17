import turtle

screen = turtle.Screen()
screen.bgcolor("white")
flower = turtle.Turtle()
flower.speed(10)
flower.pencolor("purple")

def draw_petal():
        flower.circle(100, 60)
        flower.left(120)
        flower.circle(100, 60)
        flower.left(120)

for _ in range(6):
        draw_petal()
        flower.left(60)

flower.penup()
flower.goto(0, -40)
flower.pendown()
flower.begin_fill()
flower.color("yellow")
flower.circle(40)
flower.end_fill()
flower.hideturtle()
turtle.done()