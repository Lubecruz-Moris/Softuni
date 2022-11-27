def square_summing(first, second, third, fourth):

    square_sum = first + second + third + fourth
    return square_sum


def max_square_sum(matrix):
    location = []
    highest_value = 0
    for row_index in range(0, rows_count-1, 1):
        for column_index in range(0, columns_count-1, 1):
            first_num = matrix[row_index][column_index]
            second_num = matrix[row_index + 1][column_index]
            third_num = matrix[row_index][column_index + 1]
            fourth_num = matrix[row_index + 1][column_index + 1]
            square_sum = square_summing(first_num, second_num, third_num, fourth_num)
            if square_sum > highest_value:
                highest_value = square_sum
                location = [(first_num, third_num), (second_num, fourth_num)]

    [print(x, z,  sep=" ") for x, z in location]

    print(highest_value)


rows_count, columns_count = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(rows_count):
    matrix.append([int(x) for x in input().split(", ")])

max_square_sum(matrix)

