days_of_adventure = int(input())
players = int(input())
energy = float(input())
water_per_day = float(input())
food_per_day = float(input())
total_water = days_of_adventure * water_per_day * players
total_food = days_of_adventure * food_per_day * players
for day in range(1, days_of_adventure + 1):

    energy_expended = float(input())
    energy -= energy_expended

    if energy <= 0:
        break

    if day % 2 == 0:
        energy += energy * 0.05
        total_water -= total_water * 0.3

    if day % 3 == 0:
        total_food -= total_food / players
        energy += energy * 0.1

if energy > 0:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")

else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
