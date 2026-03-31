import turtle 
turtle.Screen().bgcolor("white")
turtle.Screen().setup(1000,1000)
turtle.color("red")
polygon = turtle.Turtle()

sides = 8
length = 120
angle = 360/sides

for i in range(sides) :
    turtle.color("red")
    turtle.fillcolor("yellow")
    polygon.forward(length)
    polygon.right(angle)
turtle.done()