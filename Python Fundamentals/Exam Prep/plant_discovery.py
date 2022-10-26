count_of_plants = int(input())
plant_dict = {}
for i in range(count_of_plants):
    data = input().split("<->")
    plant = data[0].lower()
    rarity = data[1]
    plant_dict[plant] = [rarity, 0.00, 0]

while True:
    command = input()
    if command == "Exhibition":
        break
    command = command.split(": ")
    values = command[1].split(" - ")
    current_plant = values[0].lower()
    if current_plant in plant_dict:
        if command[0] == "Rate":
            rating = float(values[1])
            if rating > 0:
                plant_dict[current_plant][1] += rating
                plant_dict[current_plant][2] += 1
        elif command[0] == "Update":
            new_rarity = values[1]
            plant_dict[current_plant][0] = new_rarity
        elif command[0] == "Reset":
            plant_dict[current_plant][1] = 0.00
    else:
        print("error")

print("Plants for the exhibition:")
for plants in plant_dict:
    average_rating = 0
    if plant_dict[plants][1] > 0:
        average_rating = plant_dict[plants][1] / plant_dict[plants][2]
    print(f"- {plants[0].upper()+plants[1:]}; Rarity: {plant_dict[plants][0]}; Rating: {average_rating:.2f}")
