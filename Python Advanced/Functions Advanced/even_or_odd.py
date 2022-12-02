def even_odd(*args):
    parity = 0 if args[-1] == "even" else 1
    result = []
    for value in args[:-1]:
        if value % 2 == parity:
            result.append(value)
    return result

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))