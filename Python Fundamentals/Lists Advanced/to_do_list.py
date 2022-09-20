command = input()

list = [0 for num in range(11)]
while command != "End":
    explode = command.split("-")
    priority = int(explode[0])
    note = explode[1]
    list[priority] = note
    command = input()

result = [element for element in list if element != 0]

print(result)