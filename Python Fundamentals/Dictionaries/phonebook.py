phonebook = {}

while True:
    command = input()
    if len(command) == 1:
        break
    info = command.split("-")
    name = info[0]
    number = info[1]
    phonebook[name] = number
count = int(command)
for n in range(count):
    search = input()
    if search in phonebook.keys():
        print(f"{search} -> {phonebook[search]}")
    else:
        print(f"Contact {search} does not exist.")
