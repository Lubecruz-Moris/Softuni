number = int(input())
for rows in range(1, number +1):
    for columns in range(0, rows):
        print("*", end="")
    print("")
for rows in range(number-1, 0, -1):
    for columns in range(0, rows):
        print("*", end="")
    print("")