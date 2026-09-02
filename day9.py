#TUPLES BASIC
"""
a=(2,4,5,76)
b=(4)
print(a)
print(type(a))
print(type(b))

#tuple unpacking 1
t=(4,5,60)
a,b,c=t
print(a)
print(b)
print(c)

#tuple unpacking 2
t1=(10,20,30,40,50)
a,*b=t1
print(a)
print(b)

#tuple unpacking 3
t2=(10,20,30,40,50)
a,*b,c=t2
print(a)
print(b)
print(c)
"""
#Tuple Creation & Unpacking
"""
p=(3,4)
print(p[0])
x,y=p
print(x,y)
colors="green","red","blue","yellow"  #parienthesis are optional
print(colors)
"""

#swapping
"""
a,b=4,5
print("Before Swapping:",a,b)
a,b=b,a
print("After swapping:",a,b)
"""
#TRY EXPECT
#try      → Try this code
#except   → If error happens, handle it
#else     → If no error, do this
#finally  → Always do this
"""
try:
    a=2
    b=3
    print(a/b)
except:
    print("The code is wrong")
else:
    print("The code has no error")
finally:
    print("code completed")
"""
#Tuple vs List Immutability
"""
list=[1,2,3,4,5,9]
tuple=(4,7,6,3,3,8)
try:
    tuple[0]=9
except TypeError as e:
    print("error:",e)
list[0]=9
print("list after change",list)
"""

#count and index
"""
tu=(3,5,7,66,4,3,7.8,3)
print(tu.count(3))
print(tu.index(7))
"""

#list to tuple and tuple to list
"""
list_fruits=["apple","banana","grapes","kiwi"]
to_tuple=tuple(list_fruits)
print("after converting to tuple",to_tuple)

tuple=(3,7,9,2,88,4)
to_list=list(tuple)
print("after conerting to list:",to_list)
to_list.sort()
print("after sorting",to_list)
"""

#Min/Max in a Tuple of Tuples
"""
scores=(("sruthi",99),("vikram",98),("charan",90))
maximim=max(scores,key=lambda x:x[1])
minimum=min(scores,key=lambda x:x[1])
print("highest:",maximim)
print("lowest:",minimum)
"""

#sort() changes the original list.
#sorted() creates and returns a new sorted list.

#Set Union, Intersection & Difference
"""
a={1,2,3,4}
b={3,4,5,6}
print(sorted(a|b))
print(sorted(a.union(b)))
print(sorted(a&b))
print(sorted(a.intersection(b)))
print(sorted(a-b))
"""

#symmetric difference
"""
a={1,2,3,4}
b={3,4,5,6}
print(sorted(a^b))
print(sorted(a.symmetric_difference(b)))
"""

# Remove Duplicates Preserving Order
#1 slower
"""
a=[3,1,3,2,1,5]
r=[]
for i in a:
    if i not in r:
        r.append(i)
print(r)
#2 faster
a=[3,1,3,2,1,5]
s=set()
r=[]
for i in a:
    if i not in s:
        s.add(i)
        r.append(i)
print(s)
print(r)
"""

#subset and superset
"""
a={1,2,3,4,5}
b={2,3}
print(b<=a) #subset
print(a.issuperset(b)) #subset
print(a>=b) #superset
print(b.issubset(a))#supoerset
"""

#unique words
"""
sentence = "the cat and the dog chased the cat"
w=set(sentence.lower().split())
print(sorted(w))
print(len(w))
"""

#frozen set demo
fs=frozenset([1,2,3])
print(fs)
try:
    fs.add(4)
except AttributeError as e:
    print("error:",e)
dict={frozenset(["delhi","mumbai"]):1400}
print(dict[frozenset(["mumbai","delhi"])])