choice = True
while choice:
    num = int(input("Enter a number: "))
    import math
    if num >= 2:
        count = False
        for i in range(2,math.ceil(math.sqrt(num)),1):
            if num % i == 0:
                count = True
                print(str(num)+" is not a prime number.")
                break
        if count == False:
            print(str(num)+" is a prime number.")
    else:
        print("Your number must be greater than 1.")
    if input("Would you like to continue? If not, type 'n': ") == "n":
        choice = False
