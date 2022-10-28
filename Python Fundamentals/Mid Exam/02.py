routes = input().split("||")
fuel = int(input())
ammo = int(input())
for route in routes:
    explode = route.split(" ")
    command = explode[0]
    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    number = int(explode[1])
    if command == "Travel":
        if fuel >= number:
            fuel -= number
            print(f"The spaceship travelled {number} light-years.")
        else:
            print("Mission failed.")
            break
    elif command == "Enemy":
        if ammo >= number:
            ammo -= number
            print(f"An enemy with {number} armour is defeated.")
        else:
            if fuel >= number * 2:
                fuel -= number * 2
                print(f"An enemy with {number} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif command == "Repair":
        fuel += number
        ammo += number * 2
        print(f"Ammunitions added: {number * 2}.")
        print(f"Fuel added: {number}.")

