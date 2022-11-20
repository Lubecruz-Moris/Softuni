n = int(input())
matrix = []
isfound = False
for _ in range(n):
    matrix.append([x for x in input()])
special_symbol = input()
for row_index in range(n):
    if isfound:
        break
    for column_index in range(n):
        if matrix[row_index][column_index] == special_symbol:
            location = (row_index, column_index)
            isfound = True

if isfound:
    print(location)
else:
    print(f"{special_symbol} does not occur in the matrix")