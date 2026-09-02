#harshad number
n=int(input("Enter a number:"))
s=0
t=n
while(n>0):
    d=n%10
    s=s+d
    n=n//10
if(t%s==0):
    print("harshad number")
else:
    print("Not")