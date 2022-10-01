legendary_items_dict = {"Shadowmourne": {'shards': 0}, "Valanyr": {'fragments': 0}, "Dragonwrath": {'motes': 0}}
junk_materials_dict = {}
is_over = False
while True:
    command = input().split(" ")

    for quantity, material in zip(command[0::2], command[1::2]):
        quantity = int(quantity)
        material = material.lower()

        if material in ["fragments", "shards", "motes"]:
            for item, materials in legendary_items_dict.items():
                if material in legendary_items_dict[item]:
                    for nested_key in materials.keys():
                        legendary_items_dict[item][nested_key] += quantity
                        if legendary_items_dict[item][nested_key] >= 250:
                            legendary_items_dict[item][nested_key] -= 250
                            print(f"{item} obtained!")
                            is_over = True
                        break
            if is_over:
                break

        else:
            if material in junk_materials_dict:
                junk_materials_dict[material] += quantity
            else:
                junk_materials_dict[material] = quantity
    if is_over:
        break
for items, material in legendary_items_dict.items():
    for mat in material.keys():
        print(f"{mat}: {legendary_items_dict[items][mat]}")

for junk in junk_materials_dict:
    print(f"{junk}: {junk_materials_dict[junk]}")
