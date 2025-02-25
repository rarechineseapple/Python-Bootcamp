import turtle
#import colorgram
from PIL import Image
from turtle import Turtle, Screen

# colors = colorgram.extract('test.jpg', 10)
#
# color_tuples = [i.rgb for i in colors]
#
# # # Same as above
# # for i in colors:
# #     print(i.rgb)
#
#
# print (color_tuples)

image = Image.open("test.jpg")
image = image.resize((100, 50 ))  # resized for performance (Above 100 is too slow, this is for landscape pictures which still takes 5 minutes)
pixels = image.load()  # loads pixel data
width, height = image.size

timmy_turtle = Turtle()

turtle.colormode(255) # sets the color mode to RGB
timmy_turtle.speed("fastest") # or speed(0)
timmy_turtle.penup()
timmy_turtle.hideturtle()

# adjust starting position on the screen
start_x, start_y = -width * 5, height * 5  # 5 is the spacing

for y in range(height):
    for x in range(width):
        color = pixels[x, y]  # rgb tuple
        timmy_turtle.goto(start_x + x * 10, start_y - y * 10)  # dot spacing
        timmy_turtle.dot(8, color)  # draw dots with specific pixel color

turtle.done()

screen = Screen()
screen.exitonclick()