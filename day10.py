#DICTINARIES
#Create, Access & Update a Dictionary
"""
person={"name":"sruthi","age":19}
print(person["name"])
#error :print(person["sruthi"])
person["age"]=26 #updation
person["city"]="pune"  #insertion
print(person) 
"""

# Iterate Keys, Values & Items
"""
marks={"math":90,"science":89,"social":99}
for i in marks:  #loops over keys by default
    print(i)
for i in marks.values():
    print(i)
for subject,score in marks.items():
    print(f"{subject}={score}")
"""

#Safe Key Lookup with .get()
"""
person={"name":"sruthi","age":19}
print(person.get("name"))  #key exists
print(person.get("city"))  #gets none
print(person.get("city","not found"))   #not found (missing common defalut)
print("city" in person)  #membershiptest
"""

#sum of dictonary values
"""
marks={"math":90,"science":89,"social":99}
print(len(marks))
print(sum(marks.values()))
"""


# Key with the Maximum Value
"""
scores={"amit":82,"bela":23,"chad":77}
best=max(scores,key=scores.get)
print(best)
print(scores[best])
"""

# Dict from Two Lists via zip()
"""
names=["sruthi","vikram","ravi"]
age=[20,22,23]
mix=dict(zip(names,age))
print(mix)
"""

# Dictionary Comprehension
"""
sq={}
for i in range(1,11):
    sq[i]=i**2
print(sq)
"""

#character count
"""
a="banana"
ch={}
for i in a:
    if i in ch:
        ch[i]+=1
    else:
        ch[i]=1
print(ch)
"""

#word frequency counter
"""
text = "to be or not to be"
s={}
for i in text.split():
    if i in s:
        s[i]+=1
    else:
        s[i]=1
print(s)
"""
# Invert a Dictionary
"""
cap={"India":"newdelhi","china":"bhutan","soudhi":"riyadh"}
d={}
for key,value in cap.items():
    d[value]=key
print(d)
"""


#Merge Two Dictionaries
"""
cap={"India":"newdelhi","china":"bhutan","soudhi":"riyadh"}
cap1={"India":"delhi","pakistan":"islamabad","afganistan":"kabul"}
merge={**cap,**cap1}
print(merge)
"""

# Filter a Dict by Condition
"""
prices={"pen":15,"book":150,"bag":500,"pencil":5}
new={}
for key,value in prices.items():
    if value>100:
        new[key]=value
print(new)
"""

#Sort a Dict by Value
"""
prices={"pen":15,"book":150,"bag":500,"pencil":5}
s=sorted(prices.items(),key=lambda x:x[1],reverse=True)
print(s)
"""

#nested dictonary
"""
a={
    "s1":{"sru":1,"vik":2,"sa":4},
    "s2":{"dhfu":4,"dfj":8,"djfhu":90}
}
print(a["s1"]["sru"])
print(a["s2"]["dfj"])
"""

#sum and average
"""
marks={
    "amit":[34,56,78],
    "sath":[34,54,87]
}
for key,value in marks.items():
    avg=sum(value)/len(value)
    print(f"{key}:{avg}")
"""






