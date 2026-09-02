#patterns

#right angled triangle
"""
n=4
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()"""


#inverted right angles triangle
"""
n=4
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
"""

#right aligned triangle
"""
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
"""

#number trinagle
"""
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
"""

#alphabet pattern
"""
n=5
ch=65
for i in range(n+1):
    for j in range(i):
        print(chr(65+j),end="")
        ch+=1
    print()
"""

#floyd's triangle
"""
n=5
num=1
for i in range(n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print() 
"""

#pyramid
"""
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
"""

#inverted pyramid
"""
n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(2*(n-i)-1):
        print("*",end=" ")
    print()
"""


#hollow square
"""
n=5
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""

#hollow rectangle
"""
n=5 
for i in range(n):
    for j in range(i+1):
        if(i==n-1 or j==0 or  j==i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""


#diamond
"""
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(1,n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(2*(n-i)-1):
        print("*",end=" ")
    print()
"""

#number pyramid
"""
n=5
num=1
for i in range(n):
    for j in range(n-i):
        print(" ",end="  ")
    for k in range(2*i+1):
        print(num,end="  ")
        num+=1
    print()
"""

#number pyramid palindromic

n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()


#pascal's triangle
"""
n=5
num=1
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(num,end=" ")
        num=
    print()"""

