def valid_password(password):
    if 6 <= len(password) <= 10:
        length = True
    else:
        length = False
    digit_counter = 0
    false_counter = 0
    for digit in password:

        if 48 <= ord(digit) <= 57:
            digit_counter += 1
        if 33 <= ord(digit) <= 47 or 58 <= ord(digit) <= 64 or 91 <= ord(digit) <= 96 or 123 <= ord(digit) <= 126:
            false_counter = 1
        else:
            pass

    if digit_counter >= 2:
        enough_digits = True
    else:
        enough_digits = False
    if length and enough_digits and false_counter == 0:
        print("Password is valid")
    if not length:
        print("Password must be between 6 and 10 characters")

    if false_counter == 1:
        print("Password must consist only of letters and digits")
    if not enough_digits:
        print("Password must have at least 2 digits")


command = input()
valid_password(command)
