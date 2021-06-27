#Rainbow Sequencing Challenge - www.101computing.net/rainbow-sequencing-challenge
import turtle
from functions import *
window = turtle.Screen()

red = "#FF0000"
orange = "#FFA600"
yellow = "#FFFF00"
green = "#62FF00"
blue = "#1E56FC"
indigo = "#4800FF"
violet = "#CC00FF"
white = "#FFFFFF"
skyblue = "#69C5FF"

#Fill the canvas with the colour of the sky
window.bgcolor(skyblue)

#Start Drawing the rainbow...  You will have to fix this code as it is not displaying the coreect rainbow
drawCircle(0,-360,red,180)
drawCircle(0,-360,orange,170)
drawCircle(0,-360,yellow,160)
drawCircle(0,-360,green,150)

drawCircle(0,-360,blue,140)
drawCircle(0,-360,indigo,130)
drawCircle(0,-360,violet,120)
drawCircle(0,-360,skyblue,110)

drawStar(-100,130,yellow,40)
drawStar(145,130,yellow,40)

addText(0,150,"Thank you Medical Staff",white,"14pt")
addText(0,120,"and",white,"14pt")
addText(0,90,"Key Workers",white,"14pt")
