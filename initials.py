import turtle

pen = turtle.Turtle()
pen.pensize(3)
pen.speed(2)
turtle.bgcolor("pink")

# Letter C
pen.color("red")
pen.penup()
pen.goto(-200, 50)
pen.pendown()
pen.goto(-240, 50)
pen.goto(-240, -50)
pen.goto(-200, -50)

# Letter A
pen.color("darkgreen")
pen.penup()
pen.goto(-150, -50)
pen.pendown()
pen.goto(-125, 50)
pen.goto(-100, -50)
pen.penup()
pen.goto(-137, 0)
pen.pendown()
pen.goto(-113, 0)

# Letter N
pen.color("darkviolet")
pen.penup()
pen.goto(-50, -50)
pen.pendown()
pen.goto(-50, 50)
pen.goto(0, -50)
pen.goto(0, 50)

# Done
pen.hideturtle()
turtle.done()
