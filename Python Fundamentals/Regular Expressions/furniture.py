import re
expression = r'>>(?P<product>[A-Za-z]+)<<(?P<price>\d+(.?\d*)?)!(?P<quantity>\d+)'
total_money = 0
products_list = []
while True:
    text = input()
    if text == "Purchase":
        break

    result = re.finditer(expression, text)
    for match in result:

        product = match.group("product")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))
        total_money += price * quantity
        products_list.append(product)

print("Bought furniture:")
if total_money > 0:
    print("\n".join(products_list))
    print(f"Total money spend: {total_money:.2f}")
