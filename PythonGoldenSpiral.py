from turtle import *
import math

speed(0)
width(2)

mult = 600
phi = (1+(math.sqrt(5)))/2

penup()
goto((mult*phi)/2,(-1)*mult/2)
left(90)
pendown()

for i in range(4):
    forward(mult)
    left(90)
for j in range(15):
    for k in range(2):
        forward(mult)
        left(90)
        forward(mult*phi)
        left(90)
    circle(mult,90)
    mult /= phi
