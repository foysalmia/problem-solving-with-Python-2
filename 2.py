number = int(input("Input : "))

for x in range(1, number+1, 1):
    for y in range(1, x+1, 1):
        print(y, end=" ")
    print()
