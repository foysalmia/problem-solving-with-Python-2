print("Input your string here:")
data = input()
result = ""
for charct in data:
    x = ord(charct)
    if (x <= 122) and (x >= 97):
        result += chr(x-32)
    elif (x <= 90) and (x >= 65):
        result += chr(x+32)
    else:
        result += charct

print(result)
