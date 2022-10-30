capacity_of_possible_messages = int(input())
users_dict = {}
while True:
    command = input()
    if command == "Statistics":
        break
    explode = command.split("=")
    if explode[0] == "Add":
        username = explode[1]
        send = int(explode[2])
        received = int(explode[3])
        if username not in users_dict:
            users_dict[username] = [send, received]
    elif explode[0] == "Message":
        sender = explode[1]
        receiver = explode[2]
        if sender and receiver in users_dict:
            users_dict[sender][0] += 1
            users_dict[receiver][1] += 1
            if users_dict[sender][0] + users_dict[sender][1] >= capacity_of_possible_messages:
                del users_dict[sender]
                print(f"{sender} reached the capacity!")
            if users_dict[receiver][1] + users_dict[receiver][0] >= capacity_of_possible_messages:
                del users_dict[receiver]
                print(f"{receiver} reached the capacity!")
    elif explode[0] == "Empty":
        username = explode[1]
        if username == "All":
            del users_dict
            users_dict = {}
        else:
            del users_dict[username]
print(f"Users count: {len(users_dict)}")
for user in users_dict:
    sum_of_messages = sum(users_dict[user])
    print(f"{user} - {sum_of_messages}")