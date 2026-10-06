# #string palindrome
# n=input("Enter the string:")
# l=len(n)-1
# s=""
# while(l>=0):
#     s+=n[l]
#     l-=1
# if(n==s):
#     print("palindrome",n)
# else:
#     print("not")
#recurssion
# 1 o n
def count(n):
    if n==0:
        return
    count(n-1)
    print(n)
count(5)
# n to 1
def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
count(5)
#fibonacci
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fin(n-2)
print(fib(6))
