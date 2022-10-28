shelves = input().split("&")
command = input()
while command != "Done":
    explode = command.split(" | ")
    current_command = explode[0]
    book1 = explode[1]
    if current_command == "Add Book":
        if book1 not in shelves:
            shelves.insert(0, book1)
    elif current_command == "Take Book":
        if book1 in shelves:
            shelves.remove(book1)

    elif current_command == "Swap Books":
        book2 = explode[2]
        if book1 in shelves and book2 in shelves:
            book1_index = shelves.index(book1)
            book2_index = shelves.index(book2)
            shelves[book1_index], shelves[book2_index] = shelves[book2_index], shelves[book1_index]
    elif current_command == "Insert Book":
        if book1 not in shelves:
            shelves.append(book1)
    elif current_command == "Check Book":
        index = int(explode[1])
        if 0 <= index < len(shelves):
            print(f"{shelves[index]}")
    command = input()
print(", ".join(shelves))
