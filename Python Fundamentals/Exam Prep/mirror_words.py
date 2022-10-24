import re
text = input()
pattern = r"([@#])(([A-Za-z]+){3,})\1\1(([A-Za-z]+){3,})\1"
result = re.finditer(pattern, text)
mirrored_words = []
total_pairs = 0
for match in result:
    total_pairs += 1
    first_word = match.group(2)
    second_word = match.group(4)
    if first_word[::-1] == second_word:
        mirrored_words.append([first_word, second_word])
if total_pairs > 0:
    print(f"{total_pairs} word pairs found!")
else:
    print("No word pairs found!")
if len(mirrored_words) == 0:
    print("No mirror words!")
else:
    mirrored_output = []
    for mirror_pairs in mirrored_words:
        mirror = " <=> ".join(mirror_pairs)
        mirrored_output.append(mirror)
    print("The mirror words are:")
    print(", ".join(mirrored_output))