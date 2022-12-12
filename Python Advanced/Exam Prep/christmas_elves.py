from collections import deque


def hot_chocolate(elf, box, elves, boxes):
    elf = elf * 2
    elves.append(elf)
    boxes.append(box)
    return


elves = deque([int(x) for x in input().split()])
boxes = [int(x) for x in input().split()]
toys = 0
energy_used = 0
current_cycle = 0

while boxes and elves:
    current_elf = elves.popleft()
    if current_elf < 5:
        continue

    current_box = boxes.pop()
    current_cycle += 1
    if current_elf < current_box:
        hot_chocolate(current_elf, current_box, elves, boxes)
        continue

    current_toys = 1
    box_value = current_box
    if current_cycle % 3 == 0:
        box_value = current_box * 2
        if current_elf < box_value:
            hot_chocolate(current_elf, current_box, elves, boxes)
            continue
        current_toys = 2

    toys += current_toys
    energy_used += box_value
    current_elf -= box_value
    current_elf += 1
    if current_cycle % 5 == 0:
        toys -= current_toys
        current_elf -= 1
    if current_elf > 0:
        elves.append(current_elf)

print(f"Toys: {toys}")
print(f"Energy: {energy_used}")
if elves:
    print("Elves left:", end=" ")
    print(*elves, sep=", ")
if boxes:
    print("Boxes left:", end=" ")
    print(*boxes, sep=", ")
