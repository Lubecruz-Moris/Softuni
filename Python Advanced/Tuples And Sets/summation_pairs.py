from itertools import combinations
numbers = [int(x) for x in input().split()]

target = int(input())

unique_pairs = set()
iterations = 0
# for num1, num2 in combinations(numbers, 2):
#     if num1 + num2 == target:
#
#         print(f'{num1} + {num2} = {target}')
#         unique_pairs.add((num1, num2))
#
#     iterations += 1
for first_num in range(len(numbers)):
    first_number = numbers[first_num]
    second_number_list = numbers[-1:first_num:-1]
    for second_num in range(len(second_number_list)):
        second_number = second_number_list[second_num]
        if first_number + second_number == target:
            print(f"{first_number} + {second_number} = {target}")
            unique_pairs.add((first_number, second_number))
        iterations += 1

print(f"Iterations done: {iterations}")
[print(x) for x in unique_pairs]