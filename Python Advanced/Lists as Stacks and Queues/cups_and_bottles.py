from collections import deque

cups = deque(int(x) for x in input().split())
cups_copy = cups.copy()
bottles = [int(x) for x in input().split()]
wasted_litters = 0
for cup in cups:
    if len(bottles) == 1:
        if cup > bottles[-1] and len(bottles) <= 1:
            break
    while cup > 0 and len(bottles) > 0:

        cup -= 1
        bottles[-1] -= 1
        if bottles[-1] == 0 and cup > 0:
            bottles.pop()
    if cup == 0:
        cups_copy.popleft()
    if len(bottles) > 0:
        wasted_litters += bottles.pop()

if len(cups_copy) == 0:
    bottles_left = [str(x) for x in bottles]
    print(f"Bottles: {' '.join(bottles_left)}")
else:
    cups_left = [str(x) for x in cups_copy]
    print(f"Cups: {' '.join(cups_left)}")

print(f"Wasted litters of water: {wasted_litters}")