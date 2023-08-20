num = int(input("How many triangular numbers do you want to see? "))

result2 = 1
print(result2)
for i in range(num-1):
    result2 *= (i+3)
    result2 //= (i+1)
    print(result2)
