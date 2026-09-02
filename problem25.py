#logarithm of a number
import math
n=float(input("enter a number:"))
if(n<=0):
    print("enter positive number")
else:
    num=math.log(n)
    print(num)
#palindrome with strings
n=input("Enter a string")
l=len(n)
for i in range(l//2):
    if(n[i]!=n[l-i-1]):
        print(" not palindrome")
        break
else:
    print("palindrome")