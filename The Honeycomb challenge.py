#<----------------------------------------------------------------------------------------------------------------------------------------------------->
#              ----------------This is my first solution before I realized you need to use "NESTED FOR LOOPS"-----------------------
#<----------------------------------------------------------------------------------------------------------------------------------------------------->
#The honeycomb challenge - www.101computing.net/honeycomb-challenge/
import turtle
import math
myPen = turtle.Turtle()
myPen.shape("arrow")

myPen.color("#a86f14")
myPen.fillcolor("#efb456")
myPen.pensize(2)
myPen.delay(10) #Set the speed of the turtle

#A Procedue to draw a pentagonal cavity at a given (x,y) position.
def drawCavity(x,y,edgeLength):
  myPen.penup()
  myPen.goto(x,y)
  myPen.pendown()
  myPen.begin_fill()
  for i in range(0,6):
      myPen.forward(edgeLength)
      myPen.left(60)
  myPen.end_fill()    



#Main Program Starts Here
#Comlpete this code to draw a full honeycomb pattern
for x in range(-150,150,60):
  
  #little something to define my parameters
  p1 = 150
  p2 = 132
  u = x+30
  z = 20*(math.sqrt(3))
  tks = 0
  
  while(tks <= 8):
    drawCavity(x,p1,20)
    drawCavity(u,p2,20)
    p1 -= z
    p2 -= z
    tks += 1

myPen.hideturtle()

#<----------------------------------------------------------------------------------------------------------------------------------------------------->
#                 -----------------------------This is my second solution using a for loop-------------------------------------
#<----------------------------------------------------------------------------------------------------------------------------------------------------->
#both solutions give the same result(obviously), but I can't confirm if this is how they expect it to be
#The honeycomb challenge - www.101computing.net/honeycomb-challenge/
import turtle
import math
myPen = turtle.Turtle()
myPen.shape("arrow")

myPen.color("#a86f14")
myPen.fillcolor("#efb456")
myPen.pensize(2)
myPen.delay(10) #Set the speed of the turtle

#A Procedue to draw a pentagonal cavity at a given (x,y) position.
def drawCavity(x,y,edgeLength):
  myPen.penup()
  myPen.goto(x,y)
  myPen.pendown()
  myPen.begin_fill()
  for i in range(0,6):
      myPen.forward(edgeLength)
      myPen.left(60)
  myPen.end_fill()    



#Main Program Starts Here
#Comlpete this code to draw a full honeycomb pattern
for x in range(-150,150,60):
  
  #little something to define my parameters
  p1 = 150
  p2 = 132
  u = x+30
  z = 20*(math.sqrt(3))
  
  for i in range(8):
    drawCavity(x,p1,20)
    drawCavity(u,p2,20)
    p1 -= z
    p2 -= z

myPen.hideturtle()
