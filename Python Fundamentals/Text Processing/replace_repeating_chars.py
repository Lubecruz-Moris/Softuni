def replace_repeating_chars(text):
    special_char = ""
    new_text = ""

    for ch in text:
        if special_char == ch:
            continue
        else:
            special_char = ch
            new_text += ch
    print(new_text)


data = input()
replace_repeating_chars(data)
