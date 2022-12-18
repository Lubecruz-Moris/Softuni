def check_symbol(row, col):
    global total_gifts
    global decorations
    global gifts
    global cookies
    if matrix[row][col] == "D":
        total_gifts -= 1
        decorations += 1

    elif matrix[row][col] == "G":
        total_gifts -= 1
        gifts += 1
    elif matrix[row][col] == "C":
        total_gifts -= 1
        cookies += 1


def next_position(command, row, col, steps):
    if command == "up":
        return row - steps, col
    if command == "down":
        return row + steps, col
    if command == "left":
        return row, col - steps
    if command == "right":
        return row, col + steps


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


def reposition(row, col, rows, cols):
    if row < 0:
        return row % rows, col
    elif row >= rows:
        return row % rows, col
    elif col < 0:
        return row, col % cols
    elif col >= cols:
        return row, col % cols


rows, cols = [int(x) for x in input().split(", ")]
matrix = []
player_row, player_col = 0, 0
total_gifts = 0
for row in range(rows):
    row_elements = input().split()
    for col in range(cols):
        if row_elements[col] == 'Y':
            player_row, player_col = row, col
        elif row_elements[col] != '.':
            total_gifts += 1
    matrix.append(row_elements)

is_collected = False
decorations = 0
gifts = 0
cookies = 0


while True:
    if total_gifts <= 0:
        break
    command = input()
    if command == "End":
        break
    matrix[player_row][player_col] = "x"
    direction, steps = command.split("-")
    steps = int(steps)
    step = 1
    check_symbol(player_row, player_col)

    next_row, next_col = next_position(direction, player_row, player_col, step)
    for i in range(0, steps -1):
        if is_outside(next_row, next_col, rows, cols):
            next_row, next_col = reposition(next_row, next_col, rows, cols)
        check_symbol(next_row, next_col)

        matrix[next_row][next_col] = "x"
        if total_gifts <= 0 and i == steps - 2:
            player_row, player_col = next_row, next_col
            is_collected = True
            break
        next_row, next_col = next_position(direction, next_row, next_col, step)

        if is_outside(next_row, next_col, rows, cols):
            next_row, next_col = reposition(next_row, next_col, rows, cols)

    if is_collected:
        break
    check_symbol(next_row, next_col)
    player_row, player_col = next_row, next_col
matrix[player_row][player_col] = 'Y'
if total_gifts == 0:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

for row in matrix:
    print(*row, sep=" ")