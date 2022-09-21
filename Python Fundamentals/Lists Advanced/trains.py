num_wagons = int(input())
wagons = [0 for num in range(num_wagons)]

command = input()

while command != "End":
    explode = command.split(" ")
    num_people = int(explode[-1])
    action = explode[0]
    if len(explode) == 3:
        position = int(explode[-2])
    if action == "add":
        wagons[-1] += num_people
    elif action == "insert":
        wagons[position] += num_people
    elif action == "leave":
        wagons[position] -= num_people
    command = input()

print(wagons)
