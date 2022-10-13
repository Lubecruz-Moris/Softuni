import re
expression = r'>>([A-Za-z]+)<<(\d+|\d+\.\d+)!(\d+)'
total_money = 0
products_list = []
while True:
    text = input()
    if text == "Purchase":
        break

    result = re.match(expression, text)
    if result is not None:
        product = result[1]
        price = float(result[2])
        quantity = float(result[3])
        total_money += price * quantity
        products_list.append(product)

print("Bought furniture:")
if total_money > 0:
    print("\n".join(products_list))
print(f"Total money spend: {total_money:.2f}")
