all_fires = input().split("#")
water = int(input())
total_effort = 0
condition = False
total_fire = 0
print("Cells:")
for fires in all_fires:
    condition = False
    fires_within_cell = fires.split(" = ")
    if water < int(fires_within_cell[1]):
        continue
    effort = int(fires_within_cell[1]) * 0.25

    if fires_within_cell[0] == "High" and 81 <= int(fires_within_cell[1]) <= 125:
        condition = True

    elif fires_within_cell[0] == "Medium" and 51 <= int(fires_within_cell[1]) <= 80:
        condition = True

    elif fires_within_cell[0] == "Low" and 1 <= int(fires_within_cell[1]) <= 50:
        condition = True

    if condition:
        water -= int(fires_within_cell[1])
        print(f"- {fires_within_cell[1]}")
        total_fire += int(fires_within_cell[1])
        total_effort += effort
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
