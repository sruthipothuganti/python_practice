#roots and quadratic equation
#vowels or consonants
"""
a=input("enter the letter:")
if a in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")
"""

#fibonacci series
"""
n1=0
n2=1
n=int(input("enter a number\n"))
for i in range(n):
    print(n1,end=" ")
    c=n1+n2
    n1=n2
    n2=c
"""

#primes in a range
"""
s=int(input("Enter starting range:"))
e=int(input("Enter ending range:"))
for i in range(s,e+1):
    c=0
    for j in range(2,i//2+1):
        if i%j==0:
            c+=1
    if c==0 and i>1:
        print(i,end=" ")
"""

#strong number
a=int(input("Enter a number:"))
temp=a
t=0
while(a>0):
    d=a%10
    f=1
    for i in range(1,d+1):
        f=f*i
    t+=f
    temp=temp//10
if(t==temp):
    print("strong number")
else:
    print("not a strong number")






