activation_key = input()
while True:
    command = input()
    if command == "Generate":
        break
    explode = command.split(">>>")
    if explode[0] == "Contains":
        substring = explode[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif explode[0] == "Flip":
        casing = explode[1]
        start_index = int(explode[2])
        end_index = int(explode[3])
        if casing == "Upper":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() + activation_key[end_index:]
        elif casing == 'Lower':
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() + activation_key[end_index:]
        print(activation_key)
    elif explode[0] == "Slice":
        start_index = int(explode[1])
        end_index = int(explode[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
print(f"Your activation key is: {activation_key}")