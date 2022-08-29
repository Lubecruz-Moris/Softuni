lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total = 0
shield_counter = 0

for lost_fights in range(1, lost_fights_count + 1):
    is_second = False
    if lost_fights % 2 == 0:
        total += helmet_price
        is_second = True
    if lost_fights % 3 == 0:
        total += sword_price
        if is_second:
            total += shield_price
            shield_counter += 1
            if shield_counter == 2:
                total += armor_price
                shield_counter = 0
print(f"Gladiator expenses: {total:.2f} aureus")