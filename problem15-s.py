#palindrome
n=int(input("Enter a number:"))
t=n
rev=0
while(n>0):
    last=n%10
    rev=rev*10+last
    n=n//10
if(t==rev):
    print("palindrome")
else:
    print("Not a palindrome")
