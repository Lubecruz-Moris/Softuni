def get_even():
    row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    return row


rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append(get_even())

print(matrix)