#numbers divided by  both 5 and 2
i,e=1,0
while(i<=100):
    if(i%2==0 and i%5==0):
        e=e+i
    i+=1
print(e)
