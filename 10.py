number = int(input("Enter Number : "))

for x in range(1, number+1):
    for i in range(x):
        print("*", end="")
    print()

for x in range(number-1, 0, -1):
    for i in range(x):
        print("*", end="")
    print()
