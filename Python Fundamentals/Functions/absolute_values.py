numbers = input().split(" ")
abs_list = list()
for num in numbers:
    converted_num = abs(float(num))
    abs_list.append(converted_num)

print(abs_list)