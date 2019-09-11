######################################################################
# Author: Vidya Mastriyana
# Username: mastriyanag
#
# Assignment: A02: Loopy Turtles, Loopy Languages
# Purpose: To demonstrate the turtle library and loops
######################################################################
import turtle

wn = turtle.Screen()
wn.bgcolor('azure')                     # or as I like to call it, 'passive blue'.

bezel = turtle.Turtle()
bezel.hideturtle()

pen = 10                                #draws the lid/bezel of the laptop
bezel.pensize(pen)
bezel.color('black')
for side in range(4):
    bezel.forward(200)
    bezel.left(90)
    bezel.forward(200)
    bezel.left(90)
    bezel.forward(200)
bezel.penup()

bezel.color('black')            #draws the base of the laptop
bezel.pendown()
bezel.begin_fill()
for side in range(2):
    bezel.forward(200)
    bezel.right(60)
    bezel.forward(200)
    bezel.right(120)
    bezel.forward(200)
bezel.end_fill()
bezel.penup()

bezel.color('blue')                     #draws the background to the BSOD
bezel.begin_fill()
for side in range(4):
    bezel.forward(200)
    bezel.left(90)
    bezel.forward(200)
    bezel.left(90)
    bezel.forward(200)
bezel.end_fill()
bezel.penup()

# BSOD TEXT SECTION:
bezel.color("white")
bezel.setpos(-100,100)
bezel.write(":(",move=False,align='left',font=("Arial",30,("bold","normal")))
bezel.setpos(-100,50)
bezel.write("Your PC ran into a problem and needs to restart.",move=False,align='left',font=("Arial",10,("bold","normal")))
bezel.setpos(-100,40)
bezel.write("We're just collecting some error info and then we'll restart for you.",move=False,align='left',font=("Arial",7,("bold","normal")))
wn.exitonclick()

