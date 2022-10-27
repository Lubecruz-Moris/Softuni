concealed_message = input()
while True:
    command = input()
    if command == 'Reveal':
        break
    explode = command.split(":|:")
    if explode[0] == "InsertSpace":
        index = int(explode[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif explode[0] == "Reverse":
        substring = explode[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message = concealed_message + substring[::-1]
            print(concealed_message)
        else:
            print("error")
    elif explode[0] == 'ChangeAll':
        substring = explode[1]
        replacement = explode[2]
        while substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")