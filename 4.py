print("Input your string here:")
data = input()

uppercase = 0
lowercase = 0
digit = 0
symbol = 0

for charct in data:
    x = ord(charct)
    if (x <= 122) and (x >= 97):
        lowercase += 1
    elif (x <= 90) and (x >= 65):
        uppercase += 1
    elif (x <= 57) and (x >= 48):
        digit += 1
    else:
        symbol += 1

print(f"Uppercase = {uppercase}")
print(f"Lowercase = {lowercase}")
print(f"Digit = {digit}")
print(f"Symbol = {symbol}")

# Uppercase = 1
# Lowercase = 7
# Digits = 3
# Symbol = 4
