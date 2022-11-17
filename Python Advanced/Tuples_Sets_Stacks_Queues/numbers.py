first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    command_parts = input().split()
    command = command_parts[0]
    target_set = command_parts[1]
    if command == 'Add':

        if target_set == "First":
            [first_set.add(int(x)) for x in command_parts[2::]]
        else:
            [second_set.add(int(x)) for x in command_parts[2::]]
    elif command == "Remove":
        if target_set == "First":
            [first_set.remove(int(x)) for x in command_parts[2::] if int(x) in first_set]
        else:
            [second_set.remove(int(x)) for x in command_parts[2::] if int(x) in second_set]
    elif command == "Check":
        if len(first_set) > len(second_set):

            print(second_set.issubset(first_set))
            continue
        print(first_set.issubset(second_set))


print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")