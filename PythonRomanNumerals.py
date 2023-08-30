numlst = [["I",1],["V",5],["X",10],["L",50],["C",100],["D",500],["M",1000],["(extra)",5000]]
num = int(input("Enter a number between 1 and 3999: "))
partition = []
for i in range(len(str(num))):
    partition.append(int(str(num)[i])*(10**(len(str(num))-i-1)))
while 0 in partition:
    partition.remove(0)
string = ""
for i in range(len(partition)):
    count = 0
    while numlst[count][1] <= partition[i]:
        count += 1
    if int(str(partition[i])[0]) <= 3:
        string += (numlst[count-1][0])*int(str(partition[i])[0])
    elif int(str(partition[i])[0]) == 4:
        string += (numlst[count-1][0])+(numlst[count][0])
    elif int(str(partition[i])[0]) <= 8:
        string += (numlst[count-1][0])+((int(str(partition[i])[0])-5)*(numlst[count-2][0]))
    else:
        string += (numlst[count-2][0])+(numlst[count][0])
print("Using roman numerals, this number is: "+string)

    
