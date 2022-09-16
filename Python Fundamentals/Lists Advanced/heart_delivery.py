def heart_deliver(data):
    command = input()
    house = 0
    house_count = 0
    valentines_count = 0

    while command != "Love!":
        jump_command = command.split(" ")
        jump_num = int(jump_command[1])
        house += jump_num

        if house > len(data) - 1:
            house = 0

        data[house] -= 2

        if data[house] == 0:
            print(f"Place {house} has Valentine's day.")
            valentines_count += 1
            house_count += 1
        elif data[house] < 0:
            data[house] = 0
            print(f"Place {house} already had Valentine's day.")

        command = input()
    print(f"Cupid's last position was {house}.")

    if valentines_count == len(data):
        print("Mission was successful.")
    else:
        print(f"Cupid has failed {abs(house_count - len(data))} places. ")


nums = list(map(int, input().split("@")))
heart_deliver(nums)