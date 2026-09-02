#kilpmeters to meters
a=100
b=a*6.213471
print(f"{a} kilometers is euals to {b} miles")

#2 leap year
a=int(input("Enter the  year:"))
if(a%400==0):
    print("leapyear")
elif(a%4==0 and a%100!=0):
    print("leap year")
else:
    print("not leap year")
