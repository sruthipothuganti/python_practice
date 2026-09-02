"""#decimal to octal
a=int(input("Enter the decimal number:"))
oc=""
while(a>0):
    rem=a%8
    oc=str(rem)+oc
    a=a//8
print("The octal number is :",oc)

#decimal to hexadecimal
a=int(input("Enter decimal Number:"))
hexa_dig="0123456789ABCDEF"
hexa=""
while(a>0):
    rem=a%16
    hexa=hexa_dig[rem]+hexa
    a=a//16
print(hexa)"""
