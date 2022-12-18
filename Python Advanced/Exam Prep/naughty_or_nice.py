def naughty_or_nice_list(kids, *args, **kwargs):
    def find_status(param):
        unique = False
        for kid_num, kid_name in kids:
            kid_param = kid_num if isinstance(param, int) else kid_name

            if param == kid_param and unique:
                unique = False
                break
            elif param == kid_param:
                name = kid_name
                num = kid_num
                unique = True
        if unique:
            return name, num
        else:
            return None, None

    def is_unique(name, num, status):
        kids.remove((num, name))

        if status == 'Nice':
            return nice_kids.append(name)
        else:
            return naughty_kids.append(name)

    nice_kids = []
    naughty_kids = []
    for command in args:
        num, status = command.split("-")
        num = int(num)
        name, num = find_status(num)
        if name and num:
            is_unique(name, num, status)

    for name, status in kwargs.items():
        name, num = find_status(name)
        if name and num:
            is_unique(name, num, status)

    not_found = [name for _, name in kids]

    result = ''
    if nice_kids:
        result += f"Nice: {', '.join(nice_kids)}\n"
    if naughty_kids:
        result += f"Naughty: {', '.join(naughty_kids)}\n"
    if not_found:
        result += f"Not found: {', '.join(not_found)}\n"
    return result

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
