import math
result = 0
n = 10**18
for i in range(n+1):
    result += (math.comb(n,i))*(i**n)
print(result % ((83**3)*(89**3)*(97**3)))
