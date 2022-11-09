numbers_dict = {}
numbers = [float(x) for x in input().split()]
for number in numbers:
    if number not in numbers_dict:
        numbers_dict[number] = 0

    numbers_dict[number] += 1

for number, count in numbers_dict.items():
    print(f"{number:.1f} - {count} times")
