command = input().split("|")
energy, coins = 100, 100
day_over = True
for activity in command:
    actions = activity.split("-")
    number = int(actions[1])
    if actions[0] == "rest":
        energy_gain = 0
        for _ in range(number):
            if energy < 100:
                energy += 1
                energy_gain += 1

        print(f"You gained {energy_gain} energy.")
        print(f"Current energy: {energy}.")
    elif actions[0] == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if number <= coins:
            coins -= number
            print(f"You bought {actions[0]}.")
        else:
            print(f"Closed! Cannot afford {actions[0]}.")
            day_over = False
            break
if day_over:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")