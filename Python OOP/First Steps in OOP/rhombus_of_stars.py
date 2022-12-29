def get_line(i, n):
    spaces = n - 1 - i
    stars = i + 1
    return " " * spaces + ("* " * stars).strip()


def print_rhombus(n):
    [print((get_line(i, n))) for i in range(n)]
    [print((get_line(i, n))) for i in range(n - 2, -1, -1)]


print_rhombus(int(input()))

