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
# #recurssion
# #1 to n
# def count(n):
#     if n==0:
#         return
#     count(n-1)
#     print(n)
# count(5)
# # n to 1
# def count(n):
#     if n==0:
#         return
#     print(n)
#     count(n-1)
# count(5)
# #fibonacci
# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1)+fib(n-2)
# print(fib(6))

# #factorial
# def fact(n):
#   if n==0:
#     return 1
#   return n*fact(n-1)
# print(fact(5))

# #even
# def even(n):
#     if n==0:
#         return
#     even(n-1)
#     if n%2==0:
#         return n
# print(even(10))

#sum of first n natural numbers
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(5))
#sum of digits of a number
def sd(n):
  s=0
  if n==0:
    return 0
  rem=n%10
  return rem+sd(n//10)
print(sd(485))

#count the number of digits of a number
def count(n):
  c=0
  if n==0:
    return 1
  return count(n//10)+1
print(count(346573))

#product of a digits of a number
def pc(n):
   if n==0:
      return 0
   return n*pc(n//10)
print(pc(45))

#power of a number
def pow(n,m):
  if m==0:
    return 1
  return n*pow(n,m-1)
print(pow(2,3))

#printing array elements
def array(arr,i):
  if i==len(arr):
    return
  print(arr[i])
  array(arr,i+1)
arr=[10,20,30,40]
array(arr,0)

#sum of array elements
def sumarr(arr,i):
  s=0
  if len(arr)==i:
    return 0
  return arr[i]+sumarr(arr,i+1)
arr=[10,20,30,40]
print(sumarr(arr,0))

