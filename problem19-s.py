n = int(input("Enter a number: "))
s = n ** 2
digits = len(str(n))

if s % (10 ** digits) == n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")