from turtle import *
import math

size = 2500

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

    scale = 50
    x = (size/((-2)*(scale)))
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

    res = 10
    res2 = 70
    penup()
    check = True
    while check == True:
        if (scale*(plot(x)) >= (size/(-2))) and (scale*(plot(x)) <= (size/(2))):
            goto(scale*x,scale*plot(x))
            check = False
        else:
            x = x + (1/res)
    pendown()
    while ((scale*x) >= (size/(-2))) and ((scale*x) <= (size/(2))):
        if ((scale*plot(x)) >= (size/(-2))) and ((scale*plot(x)) <= (size/(2))):
            pendown()
            goto(scale*x,scale*plot(x))
            x = x + (1/res)
            if ((scale*plot(x)) < (size/(-2))) or ((scale*plot(x)) > (size/(2))):
                x = x - (1/res)
                while ((scale*plot(x)) >= (size/(-2))) and ((scale*plot(x)) <= (size/(2))):
                    goto(scale*x,scale*plot(x))
                    x = x + (1/(2*res2))
                if ((scale*plot(x)) < (size/(-2))) or ((scale*plot(x)) > (size/(2))):
                    penup()
                    while ((scale*plot(x)) < (size/(-2))) or ((scale*plot(x)) > (size/(2))):
                        x = x + (1/(2*res2))
                    goto(scale*x,scale*plot(x))
                    
            
              
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
        

    
