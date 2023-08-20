from turtle import *
import math

size = 5000

screensize(size,size)
speed(0)
width(2)

def graph():
    color("dark gray")
    forward(size/2)
    right(180)
    forward(size)
    right(180)
    forward(size/2)
    left(90)
    forward(size/2)
    right(180)
    forward(size)
    right(180)
    forward(size/2)
    right(90)
    color("black")
graph()

print("This program acts as a graphing calculator based on coefficients of different integer powers of 'x'.\n")

yesorno = True
while yesorno:
    
    power = int(input("Please enter the highest positive power of 'x': "))
    while power <= 0:
        print("Not yet!")
        power = int(input("Please enter the highest positive power of 'x': "))

    powerlist = []

    for i in range(power,-1,-1):
        coefficient = float(input("Please enter the coefficient of 'x^"+str(i)+"': "))
        powerlist.append(coefficient)
    powerlist.append(0)

    reciprocals = input("Would you like to include negative powers? If so, type 'y'. Otherwise, type anything else: ")
    if reciprocals == "y":
        repower = int(input("Please enter the highest (furthest from '0') negative power of 'x': "))
        while repower > 0:
            print("Not possible!")
            repower = int(input("Please enter the highest negative power of 'x': "))

        repower *= -1
        repowerlist = []

        for i in range(repower,0,-1):
            if i != 0:
                recoefficient = float(input("Please enter the coefficient of 'x^-"+str(i)+"': "))            
            repowerlist.append(recoefficient)
    else:
        repower = 0
        repowerlist = [0]

    trig = input("Would you like to include a trigonometric function? If so, type 'y'. Otherwise, type anything else: ")
    if trig == "y":
        trigfunc = input("If you would like to use 'sine', type 's'. If 'cosine', type 'c'. If 'tangent', type 't': ")
        trigmult = float(input("Please enter the multiplier for this function: "))
    
    n = 0.01
    def plot1(n):
        global y
        y = 0
        for j in range(power+1):
            y += (powerlist[j])*(n**(power-j))
        for k in range(repower):
            y += (repowerlist[k])*(1/(n**(repower-k)))
        if trig == "y":
            if trigfunc == "s":
                y += trigmult*(math.sin(n))
            if trigfunc == "c":
                y += trigmult*(math.cos(n))
            if trigfunc == "t":
                y += trigmult*(math.tan(n))
        return y
    
    if (repower != 0):
        while (50*(plot1(n)) > ((size/2)+500)) or (50*(plot1(n)) < ((-1)*((size/2)+500))) or (50*(n) > ((size/2)+500)) or (50*(n) < ((-1)*((size/2)+500))):
            n += 0.01
        if n != 0.01:
            n -= 0.01
    else:
        n = 0
        
    buffer = n

    x = n
    def plot(x):
        global y
        y = 0
        for j in range(power+1):
            y += (powerlist[j])*(x**(power-j))
        for k in range(repower):
            y += (repowerlist[k])*(1/(x**(repower-k)))
        if trig == "y":
            if trigfunc == "s":
                y += trigmult*(math.sin(x))
            if trigfunc == "c":
                y += trigmult*(math.cos(x))
            if trigfunc == "t":
                y += trigmult*(math.tan(x))
        return y

    penup()
    goto(x*50,50*(plot(x)))
    pendown()
    while (50*(plot(x+0.05)) <= ((size/2)+500)) and (50*(plot(x+0.05)) >= ((-1)*((size/2)+500))) and (50*(x+0.05) <= ((size/2)+500)) and (50*(x+0.05) >= ((-1)*((size/2)+500))):
        x += 0.05
        goto(x*50,50*(plot(x)))
    penup()
    x = 0
    if repower != 0:
        x = (-1)*(buffer)
    goto(x*50,50*(plot(x)))
    pendown()
    while (50*(plot(x-0.05)) <= ((size/2)+500)) and (50*(plot(x-0.05)) >= ((-1)*((size/2)+500))) and (50*(x-0.05) <= ((size/2)+500)) and (50*(x-0.05) >= ((-1)*((size/2)+500))):
        x -= 0.05
        goto(x*50,50*(plot(x)))
          
    choice = input("Would you like to continue? If so, type 'y'. Otherwise, type anything else: ")

    if choice != "y":
        yesorno = False
        done()
    else:
        choice1 = input("Would you like to keep your first graph? If so, type 'y'. Otherwise, type anything else: ")
        if choice1 != "y":
            resetscreen()
            speed(0)
            width(2)
            graph()
        

    
