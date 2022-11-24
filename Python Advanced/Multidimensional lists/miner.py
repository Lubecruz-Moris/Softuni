def next_position(row, col, command):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


size = int(input())
commands = input().split()
miner_row = 0
miner_col = 0
matrix = []
collected_coal = 0
coal_to_collect = 0
for row in range(size):
    row_elements = list(input().split())
    for col in range(size):
        if row_elements[col] == "s":
            miner_row = row
            miner_col = col
        elif row_elements[col] == "c":
            coal_to_collect += 1
    matrix.append(row_elements)


game_ended = False
lost = False

for command in commands:
    next_row, next_col = next_position(miner_row, miner_col, command)
    if is_outside(next_row, next_col, size):
        continue
    matrix[miner_row][miner_col] = "*"
    if matrix[next_row][next_col] == "c":
        collected_coal += 1
        coal_to_collect -= 1

        if coal_to_collect == 0:
            game_ended = True
    elif matrix[next_row][next_col] == "e":
        game_ended = True
        lost = True
    miner_row, miner_col = next_row, next_col
    matrix[miner_row][miner_col] = "s"
    if game_ended:
        break

if lost:
    print(f"Game over! ({miner_row}, {miner_col})")
elif coal_to_collect == 0:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
elif coal_to_collect != 0:
    print(f"{coal_to_collect} pieces of coal left. ({miner_row}, {miner_col})")