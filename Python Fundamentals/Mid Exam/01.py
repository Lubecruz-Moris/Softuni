from math import ceil
budget = float(input())
students = int(input())
price_for_flour = float(input())
price_for_egg = float(input())
price_for_egg *= 10
price_for_apron = float(input())
bonus_aprons = ceil(students + students * 0.2)
flour_count = 0
total = 0
for student in range(students):
    flour_count += 1
    if flour_count == 5:
        total -= price_for_flour
        flour_count = 0
total += price_for_apron * bonus_aprons + price_for_egg * students + price_for_flour * students
money_left = abs(total - budget)
if total <= budget:
    print(f"Items purchased for {total:.2f}$.")
else:
    print(f"{money_left:.2f}$ more needed.")