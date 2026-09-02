# decimal to binary 

n=int(input("Enter a decimal number"))
binary=" "
while(n>0):
    r=n%2
    binary=str(r)+binary
    n=n//2
print(binary)


#binary to decimal
"""
n=int(input("Enter a binary number:"))
pow=0
decimal=0
while(n>0):
    r=n%10
    decimal=decimal+r*(2**pow)
    n=n//10
    pow+=1
print(decimal)"""

#Digital root
"""
n=int(input("Enter a number:"))
while(n>=10):
    s=0
    while(n>0):
        r=n%10
        s=s+r
        n=n//10
    n=s
print(s)"""


#Collatz Sequence
"""
n=int(input("Enter a number:"))
steps=0
while(n!=1):
    print(n,end=" ")
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
    steps+=1
print(f"\nsteps taken:{steps}")"""

#number guessing
"""
secret=6
attempts=0
while True:
    guess=int(input("Guess the number between 1-10:"))
    attempts+=1
    if secret<guess:
        print("NUmber is low!")
    elif secret>guess:
        print("Number is high!")
    else:
        print(f"correct! you have took {attempts} tries")
        break
        """

#Nested Loop Coordinate Pairs
"""
n=int(input("Enter sixe of matrix"))
for i in range(n):
    for j in range(n):
        print(f"({i},{j})",end="  ")
    print()
"""





