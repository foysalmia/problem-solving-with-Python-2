data = int(input("Enter how many number : "))
numbers = [0, 1]
i = 0
for x in range(data-2):
    tmp = numbers[i]+numbers[i+1]
    numbers.append(tmp)
    i += 1

for x in numbers:
    print(x, end=" ")


# 0  1  1  2  3  5  8  13  21  34
