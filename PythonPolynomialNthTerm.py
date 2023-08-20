import math, fractions
print("This program takes in the first few terms of a polynomial sequence and calculates the expression for the nth term. When typing a non-whole number, type the equivalent improper fraction. To stop entering terms, type 'n'.")
choice = True
while choice == True:
    check = False
    while check == False:
        sequence = [[]]
        while (len(sequence[0]) == 0)or(sequence[0][len(sequence[0])-1] != "n"):
            sequence[0].append(input("Enter term "+str(len(sequence[0])+1)+" of this sequence: "))
        sequence[0].remove("n")
        for i in range(len(sequence[0])):
            if "/"in sequence[0][i]:
                num = ""
                den = ""
                c = 0
                while sequence[0][i][c] != "/":
                    num += sequence[0][i][c]
                    c += 1
                c += 1
                while c < len(sequence[0][i]):
                    den += sequence[0][i][c]
                    c += 1
                sequence[0][i] = fractions.Fraction(int(num),int(den))
            else:
                sequence[0][i] = int(sequence[0][i])
        for h in range(len(sequence[0])-1):
            sequence.append([])
            for i in range(len(sequence[len(sequence)-2])-1):
                sequence[len(sequence)-1].append((sequence[len(sequence)-2][i+1])-(sequence[len(sequence)-2][i]))
        check = True
        if sequence[len(sequence)-1][0] != 0:
            check = False
            print("There are either not enough terms or this is not a polynomial! Try again!\n")
    result = []
    count = 1
    while not(min(sequence[0]) == max(sequence[0]) == 0):
        for i in range(len(sequence)):
            for j in range(len(sequence[i])):
                if min(sequence[i]) == max(sequence[i]):
                    result.append([fractions.Fraction(sequence[i][0],math.factorial(i)),i])
                    break
            if len(result) == count:
                break
        sequence = [sequence[0]]
        for i in range(len(sequence[0])):
            sequence[0][i] -= (result[len(result)-1][0])*((i+1)**(result[len(result)-1][1]))
        for i in range(len(sequence[0])):
            if sequence[0][i] % 1 == 0:
                sequence[0][i] = int(sequence[0][i])
        for h in range(len(sequence[0])-1):
            sequence.append([])
            for i in range(len(sequence[len(sequence)-2])-1):
                sequence[len(sequence)-1].append((sequence[len(sequence)-2][i+1])-(sequence[len(sequence)-2][i]))
        for i in range(len(result)):
            if result[i][0] % 1 == 0:
                result[i][0] = int(result[i][0])
        count += 1
    for i in range(len(result)):
        if result[i][0] % 1 != 0:
            result[i][0] = "("+str((result[i][0]).numerator)+"/"+str((result[i][0]).denominator)+")"
        else:
            result[i][0] = str(result[i][0])
        if i == 0:
            if ("-"in result[i][0]):
                result[i][0] = result[i][0].replace("-","")
                result[i][0] = "-"+result[i][0]
            if (result[i][0] == "1")or(result[i][0] == "-1"):
                result[i][0] = result[i][0].replace("1","")
        elif (int(result[i][1]) > 0):
            if ("-"in result[i][0]):
                result[i][0] = result[i][0].replace("-","")
                result[i][0] = " - "+result[i][0]
            else:
                result[i][0] = " + "+result[i][0]
            if (result[i][0] == " + 1")or(result[i][0] == " - 1"):
                result[i][0] = result[i][0].replace("1","")
        else:
            if ("-"in result[i][0]):
                result[i][0] = result[i][0].replace("-","")
                result[i][0] = " - "+result[i][0]
            else:
                result[i][0] = " + "+result[i][0]
        if result[i][1] > 1:
            result[i][1] = str(result[i][1])
            result[i][0] += "n^"
        elif result[i][1] == 1:
            result[i][1] = ""
            result[i][0] += "n"
        else:
            result[i][1] = ""
    print("The nth term of your sequence is: ",end="")
    for i in range(len(result)):
        print(result[i][0]+result[i][1],end="")
    print()
    if input("Would you like to repeat the program for another sequence? If not, type 'n'. Otherwise, type anything else: ") == "n":
        choice = False

