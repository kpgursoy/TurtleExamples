import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_square = turtle.Turtle()

# turtle_instance = turtle.Turtle()
# for i in range(5):
#    turtle_instance.forward(150)
#    turtle_instance.left(144)

a = 25

for i in range(10):
    for x in range(4):
        turtle_square.forward(a)
        turtle_square.right(90)
    a = a+25
turtle.done()
