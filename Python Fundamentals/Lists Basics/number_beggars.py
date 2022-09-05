offers = [int(num) for num in input().split(", ")]
number_of_beggars = int(input())
counter = 0
beggars_list = [0] * number_of_beggars
for offer in offers:
    beggars_list[counter] += offer
    counter += 1
    if counter >= number_of_beggars:
        counter = 0
print(beggars_list)