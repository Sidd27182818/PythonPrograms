import math
choice = input("This program approximates the values of sin(x) (type 's'), cos(x) (type 'c'), or tan(x) (type 't'): ")
x = float(input("Enter your value in radians: "))
def sin(x):
    y = 0
    for i in range(80):
        y += ((-1)**(i))*((x**((2*i)+1))/(math.factorial((2*i)+1)))
    return y
def cos(x):
    y = 0
    for i in range(80):
        y += ((-1)**(i))*((x**(2*i))/(math.factorial(2*i)))
    return y
if choice == "s":
    print(sin(x))
elif choice == "c":
    print(cos(x))
elif choice == "t":
    print(sin(x)/cos(x))
