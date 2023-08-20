import fractions
num = int(input("Enter a number: "))
count = 0
while fractions.Fraction(count*(count+1),2) <= num:
    count += 1
count -= 1
count1 = 0
for i in range(1,count):
    if fractions.Fraction((num - fractions.Fraction(i*(i+1),2)),i+1) % 1 == 0:
        count1 += 1
print(count1)
