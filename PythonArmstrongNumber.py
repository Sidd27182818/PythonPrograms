num = int(input("Enter a number: "))
check = 0
for i in range(len(str(num))):
    check += (int((str(num))[i]))**len(str(num))
if num == check:
    print(str(num)+" is an Armstrong number.")
else:
    print(str(num)+" is not an Armstrong number.")
