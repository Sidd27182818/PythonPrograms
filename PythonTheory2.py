print("This program calculates the (n)th term of the sequence formed by the (x)th differences of the '1/n' sequence.")

yesorno = True
while yesorno:
    x = int(input("\nPlease enter 'x': "))
    while x < 1:
        print("This value must be at least 1!")
        x = int(input("Please enter 'x' again: "))

    n = int(input("Please enter the term wished to be found (n): "))
    while n < 1:
        print("This value must be at least 1!")
        n = int(input("Please enter 'n' again: "))

    xfact = 1
    for i in range(x):
        xfact *= (i+1)

    nfact1 = 1
    if n > 1:
        for i in range(n-1):
            nfact1 *= (i+1)

    nxfact = 1
    for i in range(n+x):
        nxfact *= (i+1)

    if nxfact % (xfact*nfact1) == 0:
        print("\nThe answer is 1/"+str(nxfact//(xfact*nfact1))+".\n")
    else:
        print("\nThe answer is "+str(xfact*nfact1)+"/"+str(nxfact)+".\n")

    choice = input("Would you like to repeat this program for different values? If so, type 'y'. Otherwise, type anything else: ")
    if choice != "y":
        yesorno = False
