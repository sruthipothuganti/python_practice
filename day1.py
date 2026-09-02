#sum of digits
"""
a=int(input("Enter a number:"))
s=0
while(a>0):
    d=a%10
    s=s+d
    a=a//10
print("sum:",s)"""

#reverese of a number
"""
a=int(input("Enter a number:"))
r=0
while (a>0):
    d=a%10
    r=r*10+d
    a=a//10
print(r)"""

#count digits in a number
"""a=int(input())
c=0
while(a>0):
    d=a%10
    c=c+1
    a=a//10
print(c)"""

#power of a number without **
"""
base=4
power=6
res=1
while(power>0):
    res=res*base
    power=power-1
print(res)"""

#palindrome number
"""
a=int(input("Enter a number:"))
rev=0
temp=a
while(a>0):
    d=a%10
    rev=rev*10+d
    a=a//10
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")"""

#factorial of a number
"""
a=int(input("Enter a number:"))
f=1
for i in range(1,a+1):
    f=f*i
print(f)"""

#all factors of a number
"""
a=int(input("Enter a number:"))
for i in range(1,a+1):
    if(a%i==0):
        print(i,end=", ")"""

#prime number
"""
a=int(input("enter a number:"))
c=0
if(a==2):
    print("prime")
for i in range(2,a//2+1):
    if(a%i==0):
        c=c+1
if(c==0):
    print("prime")
else:
    print("not a prime")"""

#armstrong number
"""
a=int(input("Enter a number:"))
dig=(len(str(a)))
s=0
tem=a
while(a>0):
    d=a%10
    s=s+d**dig
    a=a//10
if(s==tem):
    print("armstrong number")
else:
    print("not")"""

#perfect number
"""
a=int(input("Enter a number:"))
s=0
temp=a
for i in range(1,a):
    if(a%i==0):
        s=s+i
print(s)
if(temp==s):
    print("perfect number")
else:
    print("Not a perfect number")"""

#gcd of 2 numbers
"""
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
while(b!=0):
    r=a%b
    a=b
    b=r
print(a)"""

#LCM OF 2 NUMBERS
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
m=max(a,b)
while True:
    if(m%a==0 and m%b==0):
        print(m)
        break
    m+=1






    





