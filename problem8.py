#lcm
a=10
b=5
if(a>b):
    g=a
else:
    g=b
while(a>0 or b>0):
    if(g%a==0 and g%b==0):
        print(g)
        break
    g+=1

