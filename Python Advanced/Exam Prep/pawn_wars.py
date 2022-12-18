def get_chess_position(row, col):
    row_nums = [8, 7, 6, 5, 4, 3, 2, 1]
    col_names = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h']
    return row_nums[row], col_names[col]


size = 8
matrix = []

current_player_pos = (0, 0)

current_player = 'w'

other_player_pos = (0, 0)

other_player = 'b'

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "w":
            current_player_pos = (row, col)
        elif row_elements[col] == "b":
            other_player_pos = (row, col)

is_queen = False
is_captured = False
current_delta = -1
other_delta = 1

while not is_captured and not is_queen:
    current_player_row, current_player_col = current_player_pos
    other_player_row, other_player_col = other_player_pos
    current_player_row += current_delta
    current_player_pos = (current_player_row, current_player_col)

    if current_player_row == other_player_row and abs(current_player_col - other_player_col) == 1:
        is_captured = True
        current_player_pos = (current_player_row, other_player_col)
    elif current_player_row in (0, size - 1):
        is_queen = True
    else:

        current_player, other_player = other_player, current_player
        current_delta, other_delta = other_delta, current_delta
        current_player_pos, other_player_pos = other_player_pos, current_player_pos

player = "White" if current_player == "w" else "Black"

(row_num, col_name) = get_chess_position(*current_player_pos)
chess_position = f"{col_name}{row_num}"
if is_captured:
    print(f"Game over! {player} win, capture on {chess_position}.")
elif is_queen:
    print(f"Game over! {player} pawn is promoted to a queen at {chess_position}.")
