#1 prime number
a=int(input("Enter the number:"))
for i in range(2,a):
    if(a%i==0):
        print("not a prime number")
        break
else:
    print("prime number")
#2 prime number in a range
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
for num in range(a,b):
    for i in range(a,num):
        if(a%i==0):
            break
    else:
        print(num)