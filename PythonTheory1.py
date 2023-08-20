# By Siddhant Dongare

# Importing necessary libraries
import math
import sys
from turtle import *

# Enabling the while loop to execute
yesorno = True

# Changing settings for the turtle
speed(0)
width(2)

# Printing message to show the purpose of the program
print("This program calculates the thickness and area of a ring that any regular polygon fits perfectly in. It also calculates the area of the polygon itself. This is based on the number of sides of the polygon and its side length.\n")

# Starting the while loop so that the code can repeat if the user chooses
while yesorno == True:

    # Printing the options for the units used
    print("1. 'mm'")
    print("2. 'cm'")
    print("3. 'm'")
    print("4. 'km'\n")

    # Getting the unit used in the program
    unit = ""
    def check():
        global unit
        unit = input("Which unit is your regular polygon's side length measured in? Please type one of the quoted units above: ")
        if unit != "mm" and unit != "cm" and unit != "m" and unit != "km":
            print("I disagree.")
            check()
    check()
    
    # Getting the number of sides of the regular polygon
    def gets():
        global s
        s = int(input("How many sides does your regular polygon have? "))
        if s < 3:
            print("I disagree.")
            gets()
    gets()

    # Getting the side length of the regular polygon
    def getb():
        global b
        b = float(input("What is the side length of your regular polygon in "+unit+"? "))
        if b == 0:
            print("I disagree.")
            getb()
    getb()

    # Calculating the ring thickness and area
    x = ((1/math.cos((90*(s-2)/s)/(180/math.pi))) - (math.tan((90*(s-2)/s)/(180/math.pi))))*b/2
    ringArea = (((1/math.cos((90*(s-2)/s)/(180/math.pi)))**2) - ((math.tan((90*(s-2)/s)/(180/math.pi)))**2))*math.pi*(b**2)/4

    # Calculating the area of the regular polygon
    area = 0
    if s == 4:
        area = b ** 2
        print("The area of your regular polygon is "+str(area)+" "+unit+" squared.")
    else:
        area = s*b*b
        area = area * math.tan((((90*s)-180)/s)/(180/math.pi))
        area = area / 4

    # Printing the values for ring thickness, ring area and shape area
    print("\nThe thickness of the ring is approximately "+str(x)+" "+unit+".")
    print("The area of the ring is approximately "+str(ringArea)+" "+unit+" squared.")
    print("The area of the regular polygon is approximately "+str(area)+" "+unit+" squared.\n")

    # Drawing the shape and ring for visualisation using turtle graphics
    color("gray")
    for i in range(s):
        forward(1000/s)
        left(180-(((180*s)-360)/s))
    penup()
    forward(1000/s)
    left(180/s)
    pendown()
    color("black")
    circle((1000/s)/(2*(math.cos((90*(s-2)/s)/(180/math.pi)))))
    right(180/s)
    left(180)
    forward(500/s)
    left(180)
    circle((500/s)*(math.tan((90*(s-2)/s)/(180/math.pi))))
    
    # Asking the user whether they would like the program to repeat
    choice = input("Would you like to repeat this program for another regular polygon? If so, type 'y'. Otherwise, type anything else: ")
    if choice != "y":
        yesorno = False
        sys.exit()
    print()
    clear()

# Shutting down the turtle
bye()
done()
