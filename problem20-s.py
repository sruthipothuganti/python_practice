#neon number
n=int(input("Enter a number:"))
ns=n**2
s=0
t=n
while(ns>0):
    d=ns%10
    s=s+d
    ns=ns//10
if(s==t):
    print("neon number")
else:
    print("Not a neon number")
