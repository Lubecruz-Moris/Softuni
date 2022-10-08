import string


def valid_usernames(data):
    expected_elements = string.digits + string.ascii_letters + "_" + "-"
    for name in data:
        if len(name) < 3 or len(name) > 16:
            continue
        elif len([x for x in name if x in expected_elements]) != len(name):
            continue
        else:
            print(name)


usernames = input().split(", ")
valid_usernames(usernames)