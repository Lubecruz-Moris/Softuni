player_1, player_2 = input().split(", ")
size = 6
matrix = []
current_player = player_1
other_player = player_2

for row in range(size):
    matrix.append(input().split())

won = False
trap = False
skip_counter = 0

while True:
    move_row, move_col = [int(x[1]) for x in input().split(",")]
    if skip_counter % 2 == 1:
        skip_counter += 1
    elif skip_counter % 2 == 0 and skip_counter != 0:
        current_player, other_player = other_player, current_player
        skip_counter -= 2
        continue

    if matrix[move_row][move_col] == "E":
        won = True
        break
    elif matrix[move_row][move_col] == "T":
        trap = True
        break
    elif matrix[move_row][move_col] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        skip_counter += 1
        if skip_counter % 2 == 1 and skip_counter != 1:
            skip_counter += 1
    current_player, other_player = other_player, current_player

if won:
    print(f"{current_player} found the Exit and wins the game!")
elif trap:
    print(f"{current_player} is out of the game! The winner is {other_player}.")
