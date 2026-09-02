#butterfly pattern
"""
n=5
for i in range(n-1):
    for j in range(i+1):
        print("*",end=" ")
    for k in range(2*(n-i-2)):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(1,n-1):
    for j in range(n-i-1):
        print("*",end=" ")
    for k in range(2*i):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    print()
"""


#reverse of a string
"""
a=input("Enter a string:")
rev=a[::-1]
print(rev)
"""

#count vowels
"""
a=input("Enter a string:")
c=0
vo="aeiouAEIOU"
for i in a:
    if i in vo:
        c=c+1
print(c)
"""

#count consonants
"""
a=input("Enter a string:")
c=0
vo="aeiouAEIOU"
for i in a:
    if i.isalpha() and i not in vo:
        c+=1
print(c)
"""

#palindrome check
"""
a=input("Enter a string:")
rev=a[::-1]
if a==rev:
    print("Palindrome")
else:
    print("Not")
"""

#count the words
"""
a=input("Enter a stentence:")
words=a.split()
c=len(words)
print(c)
"""

#upper to lower,lower to upper swapping
"""
a=input("Enter a string:")
res=" "
for i in a:
    if i.isupper():
        res=res+i.lower()
    elif i.islower():
        res=res+i.upper()
    else:
        res=res+i
print(res)"""

#counting upper and lower case letters
"""
a=input("Enter a sentence:")
uc,lc=0,0
for i in a:
    if i.isupper():
        uc+=1
    elif i.islower():
        lc+=1
print("upper count:",uc)
print("lower count:",lc)
"""

#Remove all spaces
"""
a=input("Enter a string:")
res=""
for i in a:
    if i!=" ":
        res=res+i
print(res)
"""



