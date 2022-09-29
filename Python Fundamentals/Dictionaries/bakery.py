elements = input().split(" ")
bakery = {}
for el in range(0, len(elements), 2):
    product = elements[el]
    quantity = elements[el + 1]
    bakery[product] = int(quantity)

print(bakery)