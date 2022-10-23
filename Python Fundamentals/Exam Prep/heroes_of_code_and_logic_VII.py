count_of_heroes = int(input())
heroes_dict = {}
dead_heroes = []
for i in range(count_of_heroes):
    current_hero = input().split(" ")
    heroes_dict[current_hero[0]] = [int(current_hero[1]), int(current_hero[2])]

while True:
    command = input()
    if command == "End":
        break
    explode = command.split(" - ")
    action = explode[0]
    hero_name = explode[1]
    if hero_name in heroes_dict.keys():
        amount = int(explode[2])
        if action == "CastSpell":
            spell_name = explode[3]
            if heroes_dict[hero_name][1] >= amount:
                heroes_dict[hero_name][1] -= amount
                print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        elif action == "TakeDamage":
            attacker = explode[3]
            if heroes_dict[hero_name][0] >= amount + 1:
                heroes_dict[hero_name][0] -= amount
                print(f"{hero_name} was hit for {amount} HP by {attacker} and now has {heroes_dict[hero_name][0]} HP left!")
            else:
                dead_heroes.append(hero_name)
                print(f"{hero_name} has been killed by {attacker}!")
        elif action == "Recharge":
            amount_left = 0
            heroes_dict[hero_name][1] += amount
            if heroes_dict[hero_name][1] > 200:
                amount_left = heroes_dict[hero_name][1] - 200
                amount -= amount_left
                heroes_dict[hero_name][1] = 200
            print(f"{hero_name} recharged for {amount} MP!")
        elif action == "Heal":
            amount_left = 0
            heroes_dict[hero_name][0] += amount
            if heroes_dict[hero_name][0] > 100:
                amount_left = heroes_dict[hero_name][0] - 100
                amount -= amount_left
                heroes_dict[hero_name][0] = 100
            print(f"{hero_name} healed for {amount} HP!")

for hero in heroes_dict.keys():
    if hero not in dead_heroes:
        print(hero)
        print(f"HP: {heroes_dict[hero][0]}")
        print(f"MP: {heroes_dict[hero][1]}")