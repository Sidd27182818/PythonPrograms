import fractions
print("This program can either find the area under the curve of a polynomial function using 2 limits for values of 'x' or find its gradient at a point.")
choice = input("To find the area under the curve, type 'i'. To find the gradient at a point, type 'd': ")
poly = []
for i in range(int(input("Enter the highest power of 'x' in your polynomial: ")),-1,-1):
    poly.append([int(input("Enter the coefficient of x^"+str(i)+": ")),i])
def f(x,lst):
    result = 0
    for i in range(len(lst)):
        result += (lst[i][0])*(x**(lst[i][1]))
    return result
res = fractions.Fraction(1,1000)
if choice == "i":
    lim1 = int(input("Enter the lower limit of 'x': "))
    lim2 = int(input("Enter the upper limit of 'x': "))
    result = 0
    while lim1+res <= lim2:
        result += ((f(lim1,poly)+f(lim1+res,poly))*res)/2
        lim1 += res
elif choice == "d":
    point = int(input("Enter the value of 'x' for the point at which the gradient of the curve is to be found: "))
    result = (f(point+res,poly)-f(point-res,poly))/(2*res)
print("The result is approximately: "+str(float(result)))
