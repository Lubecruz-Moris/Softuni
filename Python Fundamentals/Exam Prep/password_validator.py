password = input()
digit_count = 0
upper_count = 0
lower_count = 0
invalid_count = 0
command = input().split(" ")
while command[0] != "Complete":
    if command[0] == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        for ch in password:
            if ch.isdigit():
                digit_count += 1
            elif ch.islower():
                lower_count += 1
            elif ch.isupper():
                upper_count += 1
            elif not ch.isalpha() and not ch.isdigit() and "_" not in ch:
                invalid_count += 1
        if invalid_count > 0:
            print("Password must consist only of letters, digits and _!")
        if upper_count == 0:
            print("Password must consist at least one uppercase letter!")
        if lower_count == 0:
            print("Password must consist at least one lowercase letter!")
        if digit_count == 0:
            print("Password must consist at least one digit!")
    elif command[0] + " " + command[1] == "Make Upper":
        index = int(command[2])
        password = password[:index] + password[index].upper() + password[index+1:]
        print(password)
    elif command[0] + " " + command[1] == "Make Lower":
        index = int(command[2])
        password = password[:index] + password[index].lower() + password[index+1:]
        print(password)
    elif command[0] == "Insert":
        index = int(command[1])
        char = command[2]
        if index <= len(password):
            password = password[:index] + char + password[index:]
            print(password)
    elif command[0] == "Replace":
        char = command[1]
        value = int(command[2])
        if char in password:
            char_ascii = int(ord(char))
            summing = chr(abs(value + char_ascii))
            while char in password:
                password = password.replace(char, summing)
            print(password)

    command = input().split(" ")
