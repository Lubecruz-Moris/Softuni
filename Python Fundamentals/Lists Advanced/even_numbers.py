numbers_list = list(map(int, input().split(", ")))
indices_list = []
for number in numbers_list:
    even_number = False
    index_number = numbers_list.index(number)

    if number % 2 == 0 and number != 0:
        even_number = True
        if numbers_list.count(number) > 1:
            numbers_list[index_number] = 0
        if even_number:
            indices_list.append(index_number)
print(indices_list)
