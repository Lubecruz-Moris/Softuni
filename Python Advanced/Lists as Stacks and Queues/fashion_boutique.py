box_of_clothes = [int(x) for x in input().split()]
rack_weight = int(input())
rack_count = 1
current_rack = rack_weight
while box_of_clothes:

    if current_rack < box_of_clothes[-1]:
        rack_count += 1
        current_rack = rack_weight
    else:
        current_rack -= box_of_clothes.pop()

print(rack_count)