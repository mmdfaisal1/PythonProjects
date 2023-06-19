import turtle

my_turtle = turtle.Turtle()
turtle_screen = my_turtle.getscreen()
my_turtle.shape("turtle")
my_turtle.color("yellow")
turtle_screen.bgcolor("black")


# Event Handler
def move():
    my_turtle.forward(5)


# Register the event handler
turtle_screen.onkey(move, "space")

# Listen to the events
turtle_screen.listen()
turtle.done()
