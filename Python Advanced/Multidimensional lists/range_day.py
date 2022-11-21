def next_position(command, row, col, steps):
    if command == "up":
        return row - steps, col
    if command == "down":
        return row + steps, col
    if command == "left":
        return row, col - steps
    if command == "right":
        return row, col + steps


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


size = 5

matrix = []
player_row = 0
player_col = 0
targets = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "A":
            player_row = row
            player_col = col
        elif row_elements[col] == "x":
            targets += 1

    matrix.append(row_elements)

number_of_commands = int(input())
shot_targets = []

for _ in range(number_of_commands):
    command = input().split()
    direction = command[1]
    if command[0] == "shoot":
        steps = 1
        next_row, next_col = next_position(direction, player_row, player_col, steps)
        for _ in range(size):
            if is_outside(next_row, next_col, size):
                break
            elif matrix[next_row][next_col] == "x":
                targets -= 1
                matrix[next_row][next_col] = "."
                shot_targets.append([next_row, next_col])
                break
            next_row, next_col = next_position(direction, next_row, next_col, steps)

    elif command[0] == "move":
        steps = int(command[2])
        next_row, next_col = next_position(direction, player_row, player_col, steps)
        if is_outside(next_row, next_col, size) or matrix[next_row][next_col] == "x":
            continue
        matrix[player_row][player_col] = "."
        player_row, player_col = next_row, next_col
        matrix[player_row][player_col] = "A"

    if targets == 0:
        break

if targets != 0:
    print(f"Training not completed! {targets} targets left.")
else:
    print(f"Training completed! All {len(shot_targets)} targets hit.")

print(*shot_targets, sep="\n")
