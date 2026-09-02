#finding substring
"""
a=input("Enter a string:")
b=input("Enter a substring:")
f=-1
for i in range(len(a)-len(b)+1):
    if a[i:i+len(b)]==b:
        f=1
if f==1:
    print("substring found")
else:
    print("substring not found")
"""

#repalce old substring with new substring
"""
a="the cat sat on the cat mat"
old="cat"
new="dog"
for i in range(len(a)-len(old)+1):
    if a[i:i+len(old)]==old:
        a=a[:i]+new+a[i+len(old):]
        break
print(a)
"""

#capitalize first word
"""
a="sruthi pothuganti cse ds"
res=[]
cap=a.split()
for i in cap:
    res.append(i[0].upper()+i[1:])
print(" ".join(res))
"""

#character frequency
"""
a="banana"
fr={}
for i in a:
    if i in fr:
        fr[i]+=1
    else:
        fr[i]=1
print(fr)
"""

#remove duplicates
"""
a="sruthii"
b=[]
for i in a:
    if i not in b:
        b.append(i)
print("".join(b))
"""

#anagram check
"""
a=input("a:").lower()
b=input("b:").lower()
if sorted(a)==sorted(b):
    print("Anagram")
else:
    print("Not an Anagram")
"""

#longest word in a sentence
"""
a="hey sruthi how are you are you doing well being so diplomatic"
long=" "
for i in a.split():
    if len(i)>len(long):
        long=i
print("".join(long))
"""

#reverse the word order
"""
a="Python is Easy"
rev=a.split()
words=rev[::-1]
print(" ".join(words))
"""

#acronym generator
"""
a="read access memory"
acr=[]
for i in a.split():
    acr.append(i[0].upper())
print("".join(acr))
"""

# first non-repeating character
"""
a="swiss"
for i in a:
    if a.count(i)==1:
        print(i)
        break
"""


#all alphabets
"""
a="the quick brown fox jumps over the lazy dog".lower()
l=set()
for i in a:
    if i.isalpha():
        l.add(i)
if len(l)==26:
    print("pangarm")
else:
    print("not")
"""

#removing puncuations
"""
text=" hello5, world! how's it going?"
re=""
for i in text:
    if i.isalpha() or i.isdigit() or i==" ":
        re+=i
print(re)
"""











