def movements(row, col, command):
    if command == "left":
        return row, col - 1
    if command == "right":
        return row, col + 1
    if command == "up":
        return row - 1, col
    if command == "down":
        return row + 1, col


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


presents = int(input())
size = int(input())

matrix = []
santa_row = 0
santa_col = 0
nice_kids = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "S":
            santa_row = row
            santa_col = col
        elif row_elements[col] == "V":
            nice_kids += 1
    matrix.append(row_elements)

presents_received = 0

while True:
    if presents == 0 and nice_kids > 0:
        print("Santa ran out of presents!")
        break
    if nice_kids == 0:
        break
    command = input()
    if command == "Christmas morning":
        break

    next_row, next_col = movements(santa_row, santa_col, command)
    if is_outside(next_row, next_col, size):
        continue
    matrix[santa_row][santa_col] = "-"
    if matrix[next_row][next_col] == "V":
        presents -= 1
        nice_kids -= 1
        presents_received += 1
    elif matrix[next_row][next_col] == "C":
        directions = ["left", "right", "up", "down"]
        for direction in directions:
            if presents == 0:
                break
            dir_row, dir_col = movements(next_row, next_col, direction)
            if matrix[dir_row][dir_col] == "V" or matrix[dir_row][dir_col] == "X":
                presents -= 1
                if matrix[dir_row][dir_col] == "V":
                    nice_kids -= 1
                    presents_received += 1
                matrix[dir_row][dir_col] = "-"
    santa_row, santa_col = next_row, next_col

matrix[santa_row][santa_col] = "S"
for row in matrix:
    print(*row, sep=" ")
if nice_kids == 0:
    print(f"Good job, Santa! {presents_received} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
