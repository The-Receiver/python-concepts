from tkinter import *
from turtle import TurtleScreen, RawTurtle, Shape
from PIL import Image, ImageTk
import copy
# import turtleextra 

#allows non-gif images
def register_PIL(name, photoimg, screen):
    screen._shapes[name] = Shape("image", photoimg)

root = Tk()

x = root.winfo_screenwidth()
y = root.winfo_screenheight()

"""
Tk methods:
 winfo_screenwidth()
 winfo_screenheight()

 Canvas(Tk(), width, height())

Turtle methods:
 TurtleScreen(<< Tk canvas >>)
 Raw Turtle( << turtle_screen >> )
 turtle.shape()
 turtle.penup() / turtle.pendown()
 turtle.setx() / turtle.sety()
 turtle.goto()

 screen.mainloop()

<< register image >>


"""

print(x)
print(y)

canvas = Canvas(root, width=x, height=y)
canvas.pack(fill=BOTH, expand=YES)

screen = TurtleScreen(canvas)

# Note the different objects
turtle = RawTurtle(screen)
turtle2 = copy.copy(turtle)
turtle3 = copy.copy(turtle)

image = ImageTk.PhotoImage(Image.open("/home/mgfreshian/Pictures/lain bg.jpg"))
image2 = copy.copy(image)
image3 = copy.copy(image)

register_PIL("user1", image, screen)
register_PIL("user2", image2, screen)
register_PIL("user3", image3, screen)

turtle.shape("user1")
turtle.speed(10)
turtle2.speed(10)
turtle3.speed(10)

turtle3.shape("user3")
turtle2.shape("user2")

turtle.penup()
turtle2.penup()
turtle3.penup()

print(image.width())

turtle.setx(image.width())
turtle2.setx(-image2.width()/2)
turtle3.setx(100)

screen.mainloop()
