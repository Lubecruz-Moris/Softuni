def primary_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i]

    return diagonal_sum


n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])
print(primary_diagonal_sum(matrix))

