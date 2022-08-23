budget = float(input())
price_per_kg_flour = float(input())
eggs = price_per_kg_flour * 75 / 100
milk = price_per_kg_flour * 25/ 100
current_bread_count = 0
colored_eggs = 0
total = price_per_kg_flour + eggs + milk + milk * 25/ 100
while budget > total and budget > 0:
    budget -= total
    if budget < 0:
        break
        pass
    colored_eggs += 3
    current_bread_count += 1
    if current_bread_count % 3 == 0:
        colored_eggs -= current_bread_count - 2
print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
