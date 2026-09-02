#strings
a=input("Enter a story:")
if(len(a)<50):
    print(a)
else:
    print(a[:50])
    print("do you want to read more y/n")
    if 'y'==input():
        print(a)
    else:
        print("try again")
