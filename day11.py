# Phone Book: Add, Search, Delete
phone_book={}
def add(name,number):
    phone_book[name]=number
def search(name):
    return phone_book.get(name,"not found")
def delete(name):
    if name in phone_book:
        del phone_book[name]
        return "deleted"
    return "not found"
add("asha",923909)
add("jsfh",7897798)
print(search("asha"))
print(delete("asha"))
print(search("asha"))

#Group Items by Key
items = ["apple", "banana", "ant", "ball", "cat", "car"]
g={}
for i in items:
    key=i[0].lower()
    if key not in g:
        g[key]=[]
    g[key].append(i)
print(g)

#Group Items by length
items = ["apple", "banana", "ant", "ball", "cat", "car"]
g={}
for i in items:
    key=len(i)
    if key not in g:
        g[key]=[]
    g[key].append(i)
print(g)


#count items by category
items=[ 
("apple", "fruit"),
("mango","fruit"),
("potato","vegetable"),
("califlower","vegetable"),
("kiwi","fruit")
]
d={}
for item,cat in items:
    if cat in d:
        d[cat]+=1
    else:
        d[cat]=1
print(d)

#collections.counter
from collections import Counter
items = ["apple", "apple", "banana", "apple", "banana"]
d=Counter(items)
print(d)
d={}
for i in items:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

#collections.defaultdict Grouping
from collections import defaultdict
items = ["apple", "banana", "ant", "ball", "cat", "car"]
g=defaultdict(list)
for i in items:
    key=i[0]
    g[key].append(i)
print(g)


