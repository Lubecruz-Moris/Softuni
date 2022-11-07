from collections import deque

water_quantity = int(input())
people = deque()
while True:
    command = input()
    if command == 'Start':
        break
    people.append(command)
while True:
    command = input()
    if command == 'End':
        break
    elif command.startswith("refill "):
        explode = command.split(" ")
        water_quantity += int(explode[1])
    else:
        if water_quantity >= int(command):
            print(f"{people.popleft()} got water")
            water_quantity -= int(command)
        else:
            print(f"{people.popleft()} must wait")

print(f"{water_quantity} liters left")