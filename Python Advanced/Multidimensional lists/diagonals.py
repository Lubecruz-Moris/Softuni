size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])

primary = []
secondary = []
for index in range(size):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][size - 1 - index])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")