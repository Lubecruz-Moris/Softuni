quantity = int(input())
days = int(input())
christmas_spirit_count = 0
cost = 0
for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 10 != 0:
        is_tenth_day = False
    if day % 3 != 0:
        is_third_day = False
    if day % 2 == 0:
        christmas_spirit_count += 5
        cost += 2 * quantity
    if day % 3 == 0:
        christmas_spirit_count += 13
        cost += 8 * quantity
        is_third_day = True
    if day % 5 == 0:
        christmas_spirit_count += 17
        cost += 15 * quantity
        if is_third_day:
            christmas_spirit_count += 30
    if day % 10 == 0:
        christmas_spirit_count -= 20
        cost += 23
        is_tenth_day = True

if is_tenth_day:
    christmas_spirit_count -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {christmas_spirit_count}")