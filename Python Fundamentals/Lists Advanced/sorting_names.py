names = input().split(", ")
sort_names = sorted(names)
sort_names = sorted(sort_names, key=lambda name: -len(name))
print(sort_names)