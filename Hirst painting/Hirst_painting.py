###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r =color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle
from turtle import Turtle,Screen
turtle.colormode(255)
nazu=Turtle()
nazu.penup()
nazu.speed("fastest")
color_list=[(246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

nazu.setheading(225)
nazu.forward(300)
nazu.setheading(0)

number_of_dots=100

for i in range(1,number_of_dots):
    nazu.dot(20,random.choice(color_list))

    nazu.forward(50)
    if i%10==0:
        nazu.setheading(90)
        nazu.forward(50)
        nazu.setheading(180)
        nazu.forward(500)
        nazu.setheading(0)

screen=Screen()
screen.exitonclick()