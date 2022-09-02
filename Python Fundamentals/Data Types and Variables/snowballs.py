number_of_snowballs = int(input())
highest_value = 0
highest_quality = 0
highest_weight = 0
highest_distance = 0
for snowballs in range(number_of_snowballs):
    weight = int(input())
    distance_time = int(input())
    quality = int(input())
    value = (weight / distance_time) ** quality
    if value > highest_value:
        highest_value = value
        highest_quality = quality
        highest_weight = weight
        highest_distance = distance_time

print(f"{highest_weight} : {highest_distance} = {highest_value:.0f} ({highest_quality})")
