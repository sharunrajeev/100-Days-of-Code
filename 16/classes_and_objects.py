# Class is a blueprint for creating objects.
# Class names are written in pascal case.

# Objects are instances of classes.
# Objects have attributes and methods.
# Attributes are variables bound to an object.
# Methods are functions bound to an object.
# Objects name are written in lower case.

# import turtle
# timmy = turtle.Turtle()

# Another way to access a class is to use the class name.
from turtle import Turtle, Screen
# Initialising an object from the class
timmy = Turtle()
# Changes the shape to a turtle
timmy.shape("turtle")
# Change the color of the turtle
timmy.color("DeepPink4")
# Move the turtle forward by 100 pixels
timmy.forward(100)
# Draw circle
timmy.circle(radius=100)

my_screen = Screen()
# Attributes of an object are called properties.
# Attributes can be accessed using dot notation.
# Attributes of the object my_screen are :
print(my_screen.canvheight)
print(my_screen.canvwidth)
# canvas height and canvas width are properties of the object my_screen.

# Methods cam also be accessed using dot notation.
# Methods are functions bound to an object.
my_screen.exitonclick()
# exitonclick() is a method of the Screen class.
