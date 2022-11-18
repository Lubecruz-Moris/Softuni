from collections import deque
materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
presents_dict = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
crafted_presents = {}
while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()
    if current_magic == 0 and current_material == 0:
        continue
    if current_magic == 0:
        materials.append(current_material)
        continue
    if current_material == 0:
        magic_levels.appendleft(current_magic)
    multiplied_materials = current_material * current_magic
    if multiplied_materials in presents_dict:
        if presents_dict[multiplied_materials] not in crafted_presents:
            crafted_presents[presents_dict[multiplied_materials]] = 0
        crafted_presents[presents_dict[multiplied_materials]] += 1
        continue
    if multiplied_materials < 0:
        materials.append(current_material + current_magic)
    elif multiplied_materials > 0:
        materials.append(current_material + 15)


if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or ("Bicycle" in crafted_presents and "Teddy bear" in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

for toy, count in sorted(crafted_presents.items()):
    print(f"{toy}: {count}")

