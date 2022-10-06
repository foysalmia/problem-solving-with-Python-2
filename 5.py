
st1 = input("Enter String 1 :")
st2 = input("Enter String 2 :")

result = ""
i = -1
for x in st1:
    result += x
    result += st2[i]
    i -= 1
print(result)
