heroes = dict()
command = input().split(" ")
while command[0] != "End":
    hero_name = command[1]
    if command[0] == "Enroll":
        if hero_name in heroes:
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []
    elif command[0] == "Learn":
        spell_name = command[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                heroes[hero_name].append(spell_name)
    elif command[0] == "Unlearn":
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            spell_name = command[2]
            removed_spell = False
            for spells in heroes[hero_name]:
                if spells == spell_name:
                    heroes[hero_name].remove(spells)
                    removed_spell = True
                    break
            if not removed_spell:
                print(f"{hero_name} doesn't know {spell_name}")
    command = input().split(" ")
print("Heroes:")
for hero in heroes:
    spells = ", ".join(heroes[hero])
    print(f"== {hero}: {spells}")