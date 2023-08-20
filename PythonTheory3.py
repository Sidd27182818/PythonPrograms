import math
from turtle import *

speed(0)
width(2)
print("This program calculates the radius of one of the outer circles that touch the circumference of an inner circle such that 's' outer circles can fit on the circumference of the inner circle with a radius of 'l' with all of the outer circles touching each other.")

scale = 20

s = int(input("\nPlease enter the number of surrounding circles (s): "))
while s < 3:
    print("Not possible!")
    s = int(input("Please enter the number of surrounding circles again: "))
while s > 10:
    print("The display will not be able to show this amount of surrounding circles in detail!")
    s = int(input("Please enter the number of surrounding circles again: "))    
    
l = float(input("Please enter the radius of the inner circle in arbitrary units (l): "))

multiplier = (math.sin((180/s)/(180/math.pi)))
multiplier /= 1 - multiplier
radius = l * multiplier

if s == 6:
    radius = l

penup()
goto(0,(s-2)*scale*(-1))
pendown()
circle((s-2)*scale)
color("dark gray")

for i in range(s):
    penup()
    right(90)
    forward(((s-2)*scale)*multiplier*2)
    left(90)
    pendown()
    circle(((s-2)*scale)*multiplier)
    penup()
    left(90)
    forward((((s-2)*scale)*multiplier*2)+((s-2)*scale))
    right(180*(s-2)/s)
    forward((s-2)*scale)
    left(90)

dist1 = 20

goto(0,(((s-2)*scale)*multiplier*2)+((s-2)*scale)+dist1)
color("black")
style = ("Times New Roman", 15, "underline")
if l % 1 == 0:
    write(("- The inner circle radius is "+str(int(l))+" AU."), font = style, align = "center")
else:
    write(("- The inner circle radius is "+str(l)+" AU."), font = style, align = "center")
goto(0,(((s-2)*scale)*multiplier*2)+((s-2)*scale))
if radius % 1 == 0:
    write(("- The outer circle radius is also "+str(int(radius))+" AU."), font = style, align = "center")
else:
    write(("- The outer circle radius is around "+str(radius)+" AU."), font = style, align = "center")

hideturtle()
done()
