base_list = input().split(" ")
rounded_list = list()

for n in base_list:
    rounded_number = round(float(n))
    rounded_list.append(rounded_number)

print(rounded_list)