#Armstrong number
"""a=int(input("Enter the number:"))
pow=len(str(a))
t=a
s=0
for i in range(a):
    d=t%10
    s=s+d**pow
    t=t//10
if(s==a):
    print("Armstrong Number")
else:
    print("Not an armstrong Number")"""

a=int(input("enter starting number:"))
b=int(input("Enter Ending number:"))
for i in range(a,b):
    pow=len(str(i))
    t=i
    s=0
    while(t>0):
        d=t%10
        s=s+d**pow
        t=t//10
    if(i==s):
        print(i)


