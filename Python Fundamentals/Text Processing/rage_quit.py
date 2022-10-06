text = input()
text = text.replace(" ", "")
new_text = ""
new_addon = ""
unique_chars = set()

for ch in range(len(text)):
    if text[ch].isdigit() and int(text[ch]) >= 0:
        repeat = int(text[ch])
        if len(text) > ch+1:
            if text[ch+1].isdigit() and int(text[ch+1]) >= 0:
                repeat = int(text[ch] + text[ch +1])
        new_text += repeat * new_addon.upper()
        new_addon = ""
    else:
        new_addon += text[ch]
        unique_chars.add(text[ch].upper())
print(f"Unique symbols used: {len(unique_chars)}")
print(new_text)
