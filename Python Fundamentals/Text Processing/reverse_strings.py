reversed_word = ""
while True:
    command = input()
    if command == "end":
        break
    rev = reversed(command)
    for text in rev:
        reversed_word += text
    print(f"{command} = {reversed_word}")
    reversed_word = ""
