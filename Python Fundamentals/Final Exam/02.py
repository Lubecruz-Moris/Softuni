import re
pattern = r"([$%])([A-Z][a-z]{2,})\1: \[(\d+)]\|\[(\d+)]\|\[(\d+)]\|$"
count_of_inputs = int(input())
for i in range(count_of_inputs):
    data = input()
    result = re.match(pattern, data)
    if result is None:
        print("Valid message not found!")
    else:
        first_num = chr(int(result.group(3)))
        second_num = chr(int(result.group(4)))
        third_num = chr(int(result.group(5)))
        message = result.group(2)
        print(f"{message}: {first_num+second_num+third_num}")

