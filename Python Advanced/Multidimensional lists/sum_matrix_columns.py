def get_column_sums(matrix):
    column_sums = []
    for column_index in range(columns):
        column_sums.append(0)
        for row_index in range(rows):
            column_sums[-1] += matrix[row_index][column_index]

    return column_sums


rows, columns = [int(x) for x in input().split(", ")]
matrix = []


for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

[print(x) for x in get_column_sums(matrix)]