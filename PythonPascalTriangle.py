yesorno = True
while yesorno:
    num = 0

    def getnum():
        global num
        num = int(input("Please enter the amount of rows of Pascal's Triangle that you would like to see: "))
        if num < 1:
            print("This number must be at least 1!")
            getnum()
    getnum()

    pascalList = []
    for i in range(num):
        pascalList.append([1]*num)

    for j in range(1,num):
        for i in range(1,num):
            pascalList[j][i] = pascalList[j][i-1] + pascalList[j-1][i]

    for i in range(1,num):
        for j in range(i):
            del pascalList[i][num-(j+1)]
    maxLen = len(str(pascalList[(num-1)//2][(num-1)-((num-1)//2)]))
    if maxLen % 2 == 0:
        maxLen += 1

    pascalList1 = []
    for i in range(num):
        pascalList1 = []
        for j in range(i):
            pascalList1.append(pascalList[i-j][j])
        pascalList1.append(1)
        print()
        print(" "*(num-i)*((maxLen//2)+1),end="|")
        for k in range(len(pascalList1)):
            print(str(pascalList1[k]).zfill(maxLen),end="|")
        print("----->",11**i,"= 11 **",i,"-----> Sum of elements =",2**i,"= 2 **",i,end="")
    print()

    choice = input("Would you like to run this program again? If so, type 'y'. Otherwise, type anything else:")
    if choice != "y":
        yesorno = False
