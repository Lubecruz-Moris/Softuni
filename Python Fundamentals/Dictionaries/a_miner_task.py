mining = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in mining:
        mining[resource] = quantity
    else:
        mining[resource] += quantity

for keys in mining:
    print(f"{keys} -> {mining[keys]}")

