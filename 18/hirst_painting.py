# import colorgram
# colors = colorgram.extract('hirst_spot_painting.jpg', 240)
# colors_from_image = []
# for color in colors:
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     colors_from_image.append(new_color)

import turtle as te
from random import randint
colors_from_image = [(132, 164, 202), (224, 151, 101), (29, 42, 62), (204, 135, 147), (162, 60, 48), (236, 213, 87), (44, 100, 145), (137, 181, 161), (148, 65, 75), (171, 24, 31), (157, 31, 26), (50, 40, 44), (55, 45, 42), (59, 114, 98), (233, 162, 168), (237, 165, 156), (215, 81, 68), (31, 59, 53), (15, 96, 71), (201, 89, 100), (171, 188, 220), (34, 60, 105), (103, 124, 168), (19, 79, 101), (172, 201, 188), (33, 152, 208), (159, 202, 219), (92, 145, 131), (65, 66, 56), (223, 157, 25), (246, 204, 1)]
print(len(colors_from_image))

# Art
te.colormode(255)
pen = te.Turtle()
pen.shape('classic')
pen.penup()
pen.speed(10)
pen.setposition(-200.0, -150.0)
for i in range(10):
    pen.setposition(-200.0, 40.0 * i - 150)
    for j in range(10):
        pen.pendown()
        pen.color(colors_from_image[randint(0, 30)])
        pen.dot(20)
        pen.penup()
        pen.forward(50)

# Screen
sn = te.Screen()
sn.colormode(255)
sn.bgcolor((245, 244, 242))
sn.exitonclick()
