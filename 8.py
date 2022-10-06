def isPrime(x):
    tmp = False
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                tmp = True
                break
    return tmp


l = int(input("Enter L : "))
r = int(input("Enter R : "))

for x in range(l, r):
    if isPrime(x) == False:
        print(x, end=" ")
print()
