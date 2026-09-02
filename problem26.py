"""n=int(input())
students_data=[]
for i in range(n):
    print("name")
    n=input()
    print("email")
    e=input()
    print("hallticket number")
    h=input()"""
#prime number
n=int(input("Enter a numner:"))
if(n<=1):
    print("not prime")
else:
    for i in range(2,n):
        if(n%i==0):
            print("Not prime")
            break
    else:
        print("prime number")