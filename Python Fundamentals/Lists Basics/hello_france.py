items = input().split("|")
budget = float(input())
condition = False
profit = 0
total_wins = 0
for item in items:
    condition = False
    single_item = item.split("->")
    item_price = float(single_item[1])
    if budget < item_price:
        continue

    if single_item[0] == "Clothes" and item_price <= 50.00:
        condition = True

    elif single_item[0] == "Shoes" and item_price <= 35.00:
        condition = True

    elif single_item[0] == "Accessories" and item_price <= 20.50:
        condition = True

    if condition:
        budget -= item_price
        item_profit = item_price * 0.40
        profit += item_profit
        item_price += item_profit
        total_wins += item_price
        print(f"{item_price:.2f}", end=" ")

total_wins += budget
print()
print(f"Profit: {profit:.2f}")
if total_wins >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")