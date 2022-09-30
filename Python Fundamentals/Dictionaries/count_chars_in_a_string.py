chars = input()
occurrences = {}

for char in chars:
    if char != " ":
        if char not in occurrences:
            occurrences[char] = 1
        else:
            occurrences[char] += 1

for keys in occurrences:
    print(f"{keys} -> {occurrences[keys]}")
