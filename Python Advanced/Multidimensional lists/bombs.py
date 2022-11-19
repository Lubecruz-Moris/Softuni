def get_children(matrix, row, col):
    possible_children = [
        [row-1, col-1],
        [row-1, col],
        [row-1, col+1],
        [row, col-1],
        [row, col],
        [row, col+1],
        [row+1, col-1],
        [row+1, col],
        [row+1, col+1]
    ]
    result = []
    for child_row, child_col in possible_children:
        if 0 <= child_row < size and 0 <= child_col < size and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])
    return result


size = int(input())

matrix = []
alive_cells = 0
cells_sum = 0
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombs = [x for x in input().split()]

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(",")]
    power = matrix[row][col]
    if power <= 0:
        continue
    children = get_children(matrix, row, col)
    for child_row, child_col in children:
        matrix[child_row][child_col] -= power

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            cells_sum += el

print(f"Alive cells: {alive_cells}")
print(f"Sum: {cells_sum}")

for row in matrix:
    print(*row, sep=" ")