store = {}
command = input()

while command != "statistics":
    explode = command.split(": ")
    product = explode[0]
    quantity = int(explode[1])
    if product not in store:
        store[product] = quantity
    else:
        store[product] += quantity

    command = input()

print("Products in stock:")
for product in store.keys():
    print(f"- {product}: {store[product]}")
print(f"Total Products: {len(store.keys())}")
print(f"Total Quantity: {sum(store.values())}")
