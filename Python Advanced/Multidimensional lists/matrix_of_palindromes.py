from string import ascii_lowercase
rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    row_in_matrix = []
    for col in range(cols):

        first_last_letter = ascii_lowercase[row]
        middle_letter = ascii_lowercase[row + col]
        row_in_matrix.append(first_last_letter + middle_letter + first_last_letter)
    matrix.append(row_in_matrix)
for row in matrix:
    print(" ".join([x for x in row]))