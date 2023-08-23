import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("bay gaplumbaga")

myTurtle = turtle.Turtle()
myTurtle_Colors = ["green", "red", "blue"]
myTurtle.speed(0)
for i in range(20):
    myTurtle.color(myTurtle_Colors[i % 3])
    myTurtle.circle(2 * (i+1))
    myTurtle.circle(-2 * (i+1))
    myTurtle.left(10)

turtle.mainloop()
# turtle.done()
