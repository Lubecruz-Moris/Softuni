rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

flattening = [num for sublist in matrix for num in sublist]
print(flattening)