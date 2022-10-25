numbers = list(map(int, input().split(" ")))
while True:
    command = input()
    if command == "Finish":
        break
    actions = command.split(" ")
    current_command = actions[0]
    value = int(actions[1])
    if current_command == 'Add':
        numbers.append(value)
    elif current_command == "Remove":
        numbers.remove(value)
    elif current_command == "Replace":
        replacement = int(actions[2])
        to_replace = numbers.index(value)
        numbers[to_replace] = replacement
    elif current_command == "Collapse":
        for number in numbers:
            if number < value:
                numbers.insert(numbers.index(number), "none")
                numbers.remove(number)
numbers = list(map(str, numbers))
while "none" in numbers:
    numbers.remove("none")
print(" ".join(numbers))