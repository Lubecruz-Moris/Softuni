numbers = input().split(" ")
copy_nums = list(map(int, numbers))
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    current_min = min(copy_nums)
    numbers.remove(str(current_min))
    copy_nums.remove(current_min)

print(", ".join(numbers))
