#sorted list or not
"""
def sortede(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True
print(sortede([4,7,9,6]))
print(sortede([2,3,4,5,6]))
"""


#second largest number
"""
nums=[2,3,4,5,2,56,78,0]
l=0
sl=0
for i in range(len(nums)):
    if l<nums[i]:
        sl=l
        l=nums[i]
    if nums[i]!=l and sl<nums[i]:
        sl=nums[i]
print(l,sl)
"""


#remove duplicates
"""
nums=[1,2,2,3,1,4]
dp=[]
for i in nums:
    if i not in dp:
        dp.append(i)
print(dp)
"""

#seperate even and odd numbers
"""
nums=[1,2,3,4,5,6,7,8,9,10]
e=[]
o=[]
for i in nums:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(e,o)
"""

#cumilative sum
"""
nums=[1,2,3,4]
r=[]
s=0
for i in nums:
    s=s+i
    r.append(s)
print(r)
"""

#remove all occurence i in list
"""nums=[1,2,3,2,4,2]
re=[]
o=2
for i in nums:
    if i!=o:
        re.append(i)
print(re)
"""

#common elements
"""
a=[1,2,3,4]
b=[3,4,5,6]
res=[]
for i in a:
    if i in b and i not in res:
        res.append(i)
print(res)"""

#union of 2 lists
"""
a=[1,2,3,4]
b=[3,4,5,6]
union=[]
for i in a+b:
    if i not in union:
        union.append(i)
print(union)
"""

#finding duplicate elements
"""
nums=[1,2,3,2,4,1,5]
dup=[]
s=set()
for i in nums:
    if i not in dup and i in s:
        dup.append(i)
    s.add(i)
print(dup)
"""

#find the missing number
"""
nums=[1,2,4,5,6]
n=len(nums)+1
exp=(n*(n+1))//2
act=sum(nums)
print(exp-act)
"""


#move all zeroes to end
"""
nums=[0,1,0,3,6,0,34]
res=[]
for i in nums:
    if i!=0:
        res.append(i)
for i in nums:
    if i==0:
        res.append(i)
print(res)
"""









