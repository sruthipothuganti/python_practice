#factorial
f=1
n=int(input())
for i in range(1,n+1):
    f=f*i
print(f)
#strong number
s=0
n=int(input("no:"))
t=n
while(n>0):
    d=n%10
    f=1
    for i in range(1,d+1):
        f=f*i
    s=s+f
    n=n//10
if(t==s):
    print("strong number",s)
else:
    print("no",s)
