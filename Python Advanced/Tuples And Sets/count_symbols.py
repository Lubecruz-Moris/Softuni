text = input()
char_count = {}
for ch in text:
    if ch not in char_count:
        char_count[ch] = 0
    char_count[ch] += 1

for key, value in sorted(char_count.items()):
    print(f"{key}: {value} time/s")