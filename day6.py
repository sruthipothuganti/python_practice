# Count Substring Occurrences (Overlapping)
"""
string="aaaa"
substring="aa"
c=0
for i in range(len(string)-len(substring)+1):
    if string[i:i+len(substring)]==substring:
        c+=1
print(c)
print(len(string))
"""

#String Compression
"""
string="aaaabbbccd"
c=1
res=""
for i in range(len(string)):
    if (i+1<len(string) and string[i]==string[i+1]):
        c+=1
    else:
        res+=string[i]+str(c)
        c=1
print(res)
"""


# Caesar Cipher
"""
string="zoo, Hello World!"
swift=3
res=" "
for i in string:
    if i.isupper():
        res+=chr((ord(i)-ord("A")+swift)%26+ord("A"))
    elif i.islower():
        res+=chr((ord(i)-ord("a")+swift)%26+ord("a"))
    else:
        res+=i
print(res)
"""

#string rotation
"""
a="abcde"
b= "cdeae"
if(len(a)==len(b) and b in (a+a) ):
    print("rotation")
else:
    print("not")
"""


#longest sommon prefix

#maximum without max
"""
num=[2,3,4,6,3,56,7]
maxi=num[0]
for i in range(1,len(num)):
    if maxi<num[i]:
        maxi=num[i]
print(maxi)
"""

#minimum without min
"""
nums=[5,8,3,6,756,23,61]
mini=nums[0]
for i in range(1,len(nums)):
    if mini>nums[i]:
        mini=nums[i]
print(mini)
"""


#sum and average
"""
num=[10,20,30,40,50]
s=0
for i in num:
    s=s+i
print("sum=",s)
print("avg=",s/len(num))
"""

#linear search
"""
a=[5,5,2,76,8,5]
target=8
for i in range(len(a)):
    if a[i]==target:
        print("target found at:",i)
        break
else:
    print("not found")
"""

#count occurence of a value
"""
a=[1,2,3,2,4,3,2]
target=2
c=0
for i in range(len(a)):
    if target==a[i]:
        c+=1
print(c)
"""

#list of squares
"""
list=[2,3,4,5]
sq=[]
for i in list:
    sq.append(i**2)
print(sq)
"""

#swapping

list=[2,3,4,5,6]
l=0
r=len(list)-1
while(l<r):
    list[l],list[r]=list[r],list[l]
    l+=1
    r-=1
print(list)





