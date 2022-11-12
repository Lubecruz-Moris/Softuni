n = int(input())
table = set()
for _ in range(n):
    element = input().split()
    for el in element:
        table.add(el)
print(*table, sep='\n')