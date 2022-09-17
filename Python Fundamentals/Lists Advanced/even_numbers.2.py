numbers_list = list(map(int, input().split(", ")))
even_index_list = list()

for i in range(len(numbers_list)):
    if numbers_list[i] % 2 == 0:
        even_index_list.append(i)
print(even_index_list)