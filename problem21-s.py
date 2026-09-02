n=int(input("Enter a number:"))
t=n
square=n**2
d=len(str(n))
right=square%(10**d)
left=square//(10**d)
if(right+left==t):
    print("kaprekar number")
else:
    print("Not a kaprekar number")
