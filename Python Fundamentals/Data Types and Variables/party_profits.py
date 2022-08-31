from math import floor
group_size = int(input())
days_of_adventure = int(input())
coins = 0
is_third = False
for days in range(1, days_of_adventure + 1):
    if days % 10 == 0:
        group_size -= 2
    if days % 15 == 0:
        group_size += 5
    is_third = False
    coins += 50 - 2 * group_size
    if days % 3 == 0:
        coins -= 3 * group_size
        is_third = True
    if days % 5 == 0:
        coins += 20 * group_size
        if is_third:
            coins -= 2 * group_size
coins = floor(coins / group_size)
print(f"{group_size} companions received {coins} coins each.")