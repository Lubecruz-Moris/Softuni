gifts = input().split(" ")
command = input().split(" ")

while command[0] != "No" and command[1] != "Money":
    index = 0
    if command[0] == f"OutOfStock":
        gift = command[1]
        for _ in range(gifts.count(gift)):

            gifts.insert(gifts.index(gift), "None")
            gifts.remove(gift)
            if gifts.count(gift) > 0:
                gifts.index(gift)
    elif command[0] == "Required":
        index = int(command[2])
        if 0 < index < len(gifts):
            gifts[index] = command[1]
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input().split(" ")

while "None" in gifts:
    gifts.remove("None")
for i in gifts:
    print(i, end= " ")