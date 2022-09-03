lines = int(input())
capacity = 0

for litres in range(lines):
    litres_of_water = int(input())

    if litres_of_water + capacity <= 255:
        capacity += litres_of_water
        continue
    print("Insufficient capacity!")
print(capacity)