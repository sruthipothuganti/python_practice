#decimal to binary
a=int(input("Enter the decimal Number:"))
bi=""
while(a>0):
    re=a%2
    bi=str(re)+bi
    a=a//2
print(bi)