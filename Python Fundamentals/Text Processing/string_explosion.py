text = input()
new_text = list(text)
strength = 0
for ch in range(len(text)):
    if strength > 0 and text[ch] != ">":
        new_text.pop(ch)
        new_text.insert(0, "0")
        strength -= 1
    elif text[ch] == ">":
        number = int(text[ch+1])
        strength += number
while "0" in new_text:
    new_text.pop(0)
text_join = "".join(new_text)
print(text_join)

