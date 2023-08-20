import math
fact = [[]]
n = 10
for i in range(1,2*n+3):
    fact[0].append(math.factorial(i))
for h in range(len(fact[0])-1):
    fact.append([])
    for i in range(len(fact[len(fact)-2])-1):
        fact[len(fact)-1].append((fact[len(fact)-2][i+1])-(fact[len(fact)-2][i]))
for i in range(1,len(fact[n])+1):
    fact[n][i-1] //= math.factorial(i)
print(fact[n])
