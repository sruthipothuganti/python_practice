"""n=int(input("Enter a number:"))
sum=0
t=n
length=len(str(n))
while(n>0):
    rem=n%10
    sum=sum+rem**length
    length-=1
    n=n//10
if(t==sum):
    print("disarium number")
else:
    print("not")"""
#leet code 151
"""
n=input("Enter a string:")
a=n.split()
rev_sen=" ".join(a[::-1])
print(rev_sen)"""
#leet code 1480
n=[3,1,2,10,1]
s=0
li=[]
for i in range(len(n)):
    s=s+n[i]
    li.append(s)
print(li)
#leet code 1672
a=[[1,2,3],[3,2,1]]
maxwe=0
for i in range(len(a)):
    s=0
    for j in range(len(a[i])):
        s=s+a[i][j]
    if(s>maxwe):
        maxwe=s
print(maxwe)
#leetcod
s=["h","e","l","l","o"]
s[:]=s[::-1]
print(s)
#leetcode-242
s="cat"
r="act"
if sorted(s)==sorted(r):
    print(True)
else:
    print(False)
