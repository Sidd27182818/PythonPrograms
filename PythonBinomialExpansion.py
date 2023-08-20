print("This program binomially expands the expression '(kx + b)^n' in descending powers of 'x'.\n")

yesorno = True

while yesorno:
    k = int(input("Please enter 'k': "))
    b = int(input("Please enter 'b': "))   

    n = 0
    def getn(): 
        global n
        n = int(input("Please enter 'n': "))
        if n < 0:
            print("Invalid input!")
            getn()
    getn()

    binomialList = [1]*(n+1)
    for i in range(1,n+1):
        binomialList[i] = binomialList[i-1] * ((n-(i-1))/i)
        
    print("The expanded form is: ",end="")
    if k != 0 and b != 0 and n > 1:
        for i in range(n+1):
            if i == 0:
                if (k**n) != 1:
                    print(end=((str((k**n)))+"x^"+str(n)))
                else:
                    print(end="x^"+str(n))
            elif i == n:
                if ((b**i) >= 0) and ((b**i) % 1 == 0):
                    print(" + ",end=(str(int(b**i))))
                else:
                    print(" - ",end=(str(int((b**i)*(-1)))))
            elif i == (n-1):
                if (k*(b**i)*n) != 1:
                    if (k*(b**i)*n) >= 0:
                        print(" + ",end=(str(k*(b**i)*n)+"x"))
                    else:
                        print(" - ",end=(str((k*(b**i)*n)*(-1))+"x"))
                else:
                    print(" + ",end=("x"))
            else:
                if (binomialList[i]*(k**(n-i))*(b**i)) != 1:
                    if ((binomialList[i]*(k**(n-i))*(b**i)) >= 0):
                        print(" + ",end=(str(int(binomialList[i]*(k**(n-i))*(b**i)))+"x^"+str(n-i)))
                    elif ((binomialList[i]*(k**(n-i))*(b**i)) < 0):
                        print(" - ",end=(str(int((binomialList[i]*(k**(n-i))*(b**i)))*(-1))+"x^"+str(n-i)))
                else:
                    print(" + ",end=("x^"+str(n-i)))
    elif k != 0 and b != 0 and n == 1:
        if b > 0:
            print(str(k)+"x + "+str(b))
        elif b < 0:
            print(str(k)+"x - "+str(b*(-1)))
    elif k == 0 and b != 0:
        print(str(b**n))
    elif k != 0 and b == 0:
        if (k**n) != 1:
            print(str(k**n)+"x^"+str(n))
        else:
            print("x^"+str(n))
    elif k == 0 and b == 0:
        print("0")
    if n == 0:
        print("1")

    choice = input("\nWould you like to repeat this program? If so, type 'y'. Otherwise, type anything else: ")
    if choice != "y":
        yesorno = False
