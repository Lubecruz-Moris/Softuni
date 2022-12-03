def fill_the_box(height, length, width, *args):
    free_space = height * length * width
    values_left = []
    for value in args:
        if value == "Finish":
            break
        if value >= free_space:
            value -= free_space
            free_space = 0
            values_left.append(value)
        else:
            free_space -= value
    if free_space > 0:
        return f"There is free space in the box. You could put {free_space} more cubes."
    else:
        return f"No more free space! You have {sum(values_left)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))