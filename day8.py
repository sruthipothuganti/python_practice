#rotate an array
"""
n=[1,2,3,4,5]
k=2
k=k%len(n)
r=n[-k:]+n[:-k]
print(r)"""

#spliting into chunks final chunk is smaller
"""
n=[3,4,5,23,6.8,5,3]
size=3
chunks=[]
for i in range(0,len(n),size):
    chunks.append(n[i:i+size])
print(*chunks)
"""

#inserting into sorted list
"""
n=[4,7,2,9,9,4,6]
n.sort()
pos=len(n)
val=5
for i in range(len(n)):
    if val<n[i]:
        pos=i
        break
n.insert(pos,val)
print(n)
"""

#pair with a given sum
"""
n=[1,2,3,4,5,6]
target=7
for i in range(len(n)):
    for j in range(i,len(n)):
        if n[i]+n[j]==target:
            print("pair:",n[i],"+",n[j],"=",target)
"""

#merge 2 sorted lists
"""a=[1,2,3,4,5,6]
b=[9,4,7,0]
a.sort()
b.sort()
merge=[]
i=0
j=0
while(i<len(a) and j<len(b)):
    if(a[i]<=a[j]):
        merge.append(a[i])
        i+=1
    else:
        merge.append(b[j])
        j+=1
while i<len(a):
    merge.append(a[i])
    i+=1
while j<len(b):
    merge.append(b[j])
    j+=1
print(merge)"""

#flatten the list
"""
n=[[1,2,3],[3,4],[2]]
f=[]
for i in n:
    for j in i:
        f.append(j)
print(f)"""

#bubble sort
"""
a=[3,5,1,0,-1]
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)"""



