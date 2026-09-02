#string palindrome
n=input("Enter the string:")
l=len(n)-1
s=""
while(l>=0):
    s+=n[l]
    l-=1
if(n==s):
    print("palindrome",n)
else:
    print("not")
