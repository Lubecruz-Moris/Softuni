shelves = input().split("&")

while True:
    command = input()
    if command == "Done":
        break
    actions = command.split(" | ")
    current_command = actions[0]
    first_book = actions[1]

    if current_command == "Add Book":

        if first_book not in shelves:
            shelves.insert(0, first_book)

    elif current_command == "Take Book":

        if first_book in shelves:
            shelves.remove(first_book)

    elif current_command == "Swap Books":
        second_book = actions[2]

        if first_book in shelves and second_book in shelves:
            first_book_position = shelves.index(first_book)
            second_book_position = shelves.index(second_book)
            shelves[first_book_position], shelves[second_book_position] = shelves[second_book_position], shelves[first_book_position]

    elif current_command == "Insert Book":

        if first_book not in shelves:
            shelves.append(first_book)

    elif current_command == "Check Book":
        index = int(actions[1])

        if 0 <= index < len(shelves):
            print(f"{shelves[index]}")

print(", ".join(shelves))
