def find_aggressive_horse(matrix, row, col, size):
    moves = [
        [row-2, col-1],
        [row-2, col+1],
        [row-1, col+2],
        [row-1, col-2],
        [row + 2, col - 1],
        [row + 2, col + 1],
        [row + 1, col + 2],
        [row + 1, col - 2]
    ]
    result = 0
    for r, c in moves:
        if 0 <= r < size and 0 <= c < size and matrix[r][c] == "K":
            result += 1
    return result


size = int(input())

matrix = []
knights_removed = 0
for row in range(size):
    matrix.append(list(input()))

while True:
    highest_attack = 0
    knight_row = 0
    knight_col = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "0":
                continue
            current_attack = find_aggressive_horse(matrix, row, col, size)
            if current_attack > highest_attack:
                highest_attack = current_attack
                knight_row = row
                knight_col = col
    if highest_attack == 0:
        break
    matrix[knight_row][knight_col] = "0"
    knights_removed += 1

print(knights_removed)