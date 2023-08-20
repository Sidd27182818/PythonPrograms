import math
result = 0
for i in range(1,20000):
    result += 1/(i**2)
    print(math.sqrt(result*6))
