def is_invalid(commands):
    invalid = True
    if len(commands) != 5 or commands[0] != "swap":
        return invalid

    for num in commands[1:]:
        if not num.isdigit():
            return invalid


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row > rows or col > cols


rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

while True:
    command = input()
    if command == "END":
        break
    command_parts = command.split()
    if is_invalid(command_parts):
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command_parts[1:]]
    if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=" ")