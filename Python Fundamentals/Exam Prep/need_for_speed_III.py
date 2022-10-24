count_of_cars = int(input())
cars_dict = {}
for i in range(count_of_cars):
    data = input().split("|")
    model = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    cars_dict[model] = [mileage, fuel]

while True:
    command = input()
    if command == "Stop":
        break
    explode = command.split(" : ")
    car = explode[1]
    if explode[0] == "Drive":
        distance = int(explode[2])
        fuel = int(explode[3])
        if cars_dict[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car][0] += distance
            cars_dict[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car][0] >= 100000:
                del cars_dict[car]
                print(f"Time to sell the {car}!")
    elif explode[0] == "Refuel":
        fuel = int(explode[2])

        if cars_dict[car][1] + fuel > 75:
            fuel = abs(cars_dict[car][1] - 75)
            cars_dict[car][1] = 75
        else:
            cars_dict[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")
    elif explode[0] == 'Revert':
        kilometers = int(explode[2])
        cars_dict[car][0] -= kilometers
        if cars_dict[car][0] < 10000:
            cars_dict[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for cars in cars_dict:
    print(f"{cars} -> Mileage: {cars_dict[cars][0]} kms, Fuel in the tank: {cars_dict[cars][1]} lt.")