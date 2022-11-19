def next_position(command, row, col):
    if command == "up":
        return row - 1, col
    if command == "down":
        return row + 1, col
    if command == "left":
        return row, col - 1
    if command == "right":
        return row, col + 1


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


size = int(input())
matrix = []
alice_row = 0
alice_col = 0
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "A":
            alice_row = row
            alice_col = col
    matrix.append(row_elements)

tea_bags = 0


while tea_bags < 10:
    next_row, next_col = next_position(input(), alice_row, alice_col)
    matrix[alice_row][alice_col] = "*"
    if is_outside(next_row, next_col, size):
        break
    elif matrix[next_row][next_col] == "R":
        matrix[next_row][next_col] = "*"
        break
    elif matrix[next_row][next_col].isdigit():
        tea_bags += int(matrix[next_row][next_col])
    matrix[next_row][next_col] = "*"
    alice_row, alice_col = next_row, next_col
if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=" ")