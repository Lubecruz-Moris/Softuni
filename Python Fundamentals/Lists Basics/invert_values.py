numbers = input().split(" ")
inverted_list = []
for num in numbers:
    if int(num) > 0:
        inverted_list.append(-int(num))
    else:
        inverted_list.append(abs(int(num)))
print(inverted_list)
