def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])




while True:
    line = input()
    if line == "END":
        break
    command_parts = line.split()
    command = command_parts[0]
    row, col, value = [int(x) for x in command_parts[1:]]
    if is_outside(row,col, size):
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=" ")