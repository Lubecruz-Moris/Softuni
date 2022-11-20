rows, columns = [int(x) for x in input().split(", ")]
matrix = []
matrix_sum = 0
for _ in range(rows):

    nums = [int(x) for x in input().split(", ")]
    matrix.append(nums)
    matrix_sum += sum(nums)
print(matrix_sum)
print(matrix)
