deck = input().split(" ")
shuffles = int(input())
length = len(deck)
mid = int(length / 2)
for shuffle in range(shuffles):
    list = []
    for num in range(mid):
        list.append(deck[num])
        list.append(deck[mid])
        mid += 1
    deck = list
    mid = int(length / 2)
print(deck)
