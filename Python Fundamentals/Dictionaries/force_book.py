force_dict = {}
users_list = []
while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]
        if force_side not in force_dict.keys() and force_user not in users_list:
            force_dict[force_side] = [force_user]
            users_list.append(force_user)
        else:
            if force_user not in users_list:
                force_dict[force_side].append(force_user)
                users_list.append(force_user)

    elif '->' in command:
        command = command.split(" -> ")
        force_user = command[0]
        force_side = command[1]
        for side in force_dict.keys():
            if force_user in force_dict[side]:
                if len(force_dict[side]) > 1:
                    force_dict[side].remove(force_user)
                    users_list.remove(force_user)
                    break
                else:
                    del force_dict[side]
                    users_list.remove(force_user)
                    break
        if force_side not in force_dict.keys() and force_user not in users_list:
            force_dict[force_side] = [force_user]
            users_list.append(force_user)
        else:
            if force_user not in users_list:
                force_dict[force_side].append(force_user)
                users_list.append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for sides in force_dict.keys():
    print(f"Side: {sides}, Members: {len(force_dict[sides])}")
    for users in force_dict[sides]:
        print(f"! {users}")