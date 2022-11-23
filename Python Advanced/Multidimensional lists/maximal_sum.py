rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

highest_row = 0
highest_col = 0
highest_sum = float("-inf")
for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                      matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                      matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum > highest_sum:
            highest_sum = current_sum
            highest_row = row
            highest_col = col

print(f"Sum = {highest_sum}")
print(
    f"{matrix[highest_row][highest_col]} {matrix[highest_row][highest_col + 1]} {matrix[highest_row][highest_col + 2]}")
print(
    f"{matrix[highest_row + 1][highest_col]} {matrix[highest_row + 1][highest_col + 1]} {matrix[highest_row + 1][highest_col + 2]}")
print(
    f"{matrix[highest_row + 2][highest_col]} {matrix[highest_row + 2][highest_col + 1]} {matrix[highest_row + 2][highest_col + 2]}")
