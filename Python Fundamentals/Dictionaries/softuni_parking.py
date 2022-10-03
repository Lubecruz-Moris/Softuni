number_of_commands = int(input())
registered_users = {}
for users in range(number_of_commands):
    explode = input().split(" ")
    command = explode[0]
    username = explode[1]
    if command == "register":
        license_plate = explode[2]
        if username in registered_users.keys():
            print(f"ERROR: already registered with plate number {registered_users[username]}")
        else:
            registered_users[username] = license_plate
            print(f"{username} registered {registered_users[username]} successfully")
    elif command == "unregister":
        if username not in registered_users.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del registered_users[username]

for user in registered_users.keys():
    print(f"{user} => {registered_users[user]}")
