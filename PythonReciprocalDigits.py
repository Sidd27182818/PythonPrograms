def d(n,x):
    try:
        return int((str(1/x))[n+1])
    except:
        return 0
def s(n):
    result = 0
    for i in range(1,n+1):
        result += d(n,i)
        print(d(n,i))
    return result
print(s(100))
