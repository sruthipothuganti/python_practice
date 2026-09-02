#fibonacci series
a=int(input("Enter the number:"))
n1=0
n2=1
for i in range(a):
    print(n1)
    c=n1+n2
    n1=n2
    n2=c
