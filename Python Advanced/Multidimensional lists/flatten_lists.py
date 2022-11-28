values = list(input().split("|"))
result = []
for value in range(len(values) - 1, -1, -1):
    current_value = values[value].strip().split()
    result.extend(current_value)

print(" ".join(result))