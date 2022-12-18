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


def reposition(row, col, size):
    if row < 0:
        return size-1, col
    elif row >= size:
        return 0, col
    elif col < 0:
        return row, size-1
    elif col >= size:
        return row, 0
size = 6

matrix = []
rover_row, rover_col = 0, 0
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "E":
            rover_row, rover_col = row, col
    matrix.append(row_elements)

directions = input().split(", ")

water_found = False
metal_found = False
concrete_found = False

for direction in directions:
    rover_row, rover_col = next_position(direction, rover_row, rover_col)
    if is_outside(rover_row, rover_col, size):
        rover_row, rover_col = reposition(rover_row, rover_col, size)
    if matrix[rover_row][rover_col] == "W":
        water_found = True
        print(f"Water deposit found at {rover_row, rover_col}")
    elif matrix[rover_row][rover_col] == "M":
        metal_found = True
        print(f"Metal deposit found at {rover_row, rover_col}")
    elif matrix[rover_row][rover_col] == "C":
        concrete_found = True
        print(f"Concrete deposit found at {rover_row, rover_col}")
    elif matrix[rover_row][rover_col] == "R":
        print(f"Rover got broken at {rover_row, rover_col}")
        break

if water_found and metal_found and concrete_found:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")