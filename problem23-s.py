#palindrome
n=int(input("Enter a number:"))
t=n
rev=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if(t==rev):
    print("palindrome",rev)
else:
    print("Not a palindrome",rev)