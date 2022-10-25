data = input()
while True:
    command = input()
    if command == "Done":
        break
    explode = command.split(" ")
    if command == "TakeOdd":
        data = [data[el] for el in range(len(data)) if el % 2 != 0]
        data = ''.join(data)
        print(data)
    elif explode[0] == 'Cut':
        index = int(explode[1])
        length = int(explode[2])
        substring = data[index:index + length]
        data = data.replace(substring, "", 1)
        print(data)
    elif explode[0] == "Substitute":
        substring = explode[1]
        substitute = explode[2]
        if substring in data:
            while substring in data:
                data = data.replace(substring, substitute)
            print(data)
        else:
            print("Nothing to replace!")
print(f"Your password is: {data}")