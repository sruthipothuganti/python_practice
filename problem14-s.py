#printing sum of even odd number betweeen 1 to 100
i=1
es,os=0,0
while(i<=100):
    if(i%2==0):
        es=es+i
    else:
        os=os+i
    i+=1
print(es)
print(os)
