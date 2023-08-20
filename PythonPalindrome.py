palindromeStr1 = str(int(input("Please enter a whole number: ")))
palindromeStr2 = ""
for i in range(len(palindromeStr1)):
    palindromeStr2 = palindromeStr2 + (palindromeStr1[len(palindromeStr1)-(i+1)])
if palindromeStr2 == palindromeStr1:
    print("Your number is a palindrome.")
else:
    print("Your number is not a palindrome.")
