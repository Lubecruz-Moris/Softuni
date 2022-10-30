main_string = input()

while True:
    command = input()
    if command == "Done":
        break
    explode = command.split(" ")
    if explode[0] == "Change":
        char = explode[1]
        replacement = explode[2]
        while char in main_string:
            main_string = main_string.replace(char, replacement)
        print(main_string)
    elif explode[0] == "Includes":
        substring = explode[1]
        if substring in main_string:
            print(True)
        else:
            print(False)
    elif explode[0] == "End":
        substring = explode[1]
        if main_string.endswith(substring):
            print(True)
        else:
            print(False)
    elif explode[0] == "Uppercase":
        main_string = main_string.upper()
        print(main_string)
    elif explode[0] == "FindIndex":
        char = explode[1]
        if char in main_string:
            print(main_string.find(char))
    elif explode[0] == "Cut":
        start_index = int(explode[1])
        count = int(explode[2])
        main_string = main_string[start_index:start_index + count]
        print(main_string)