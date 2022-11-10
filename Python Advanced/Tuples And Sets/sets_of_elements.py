n, m = [int(x) for x in input().split()]
set1 = set()
set2 = set()

for num in range(n):
    set1.add(int(input()))

for num in range(m):
    set2.add(int(input()))

result = set1.intersection(set2)
print(*result, sep="\n")
