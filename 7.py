data = input("Input Number : ")
x = len(data)
reverseData = ""
i = -1
while i >= -1 * x:
    reverseData += data[i]
    i -= 1

if data == reverseData:
    print("True")
else:
    print("False")
