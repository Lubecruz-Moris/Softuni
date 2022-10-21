import re
text = input()
cool_threshold = 1
emoji_count = 0
cool_emojis = []
emoji_pattern = r'(:{2}|\*{2})([A-Z][a-z]{2,})\1'
emojis = re.finditer(emoji_pattern, text)
digits = re.findall(r'\d', text)
for digit in digits:
    cool_threshold *= int(digit)
for emoji in emojis:
    emoji_text = emoji.group(2)
    emoji_count += 1
    emoji_coolness = sum([ord(el) for el in emoji_text])
    if emoji_coolness >= cool_threshold:
        cool_emojis.append(emoji.group())

print(f"Cool threshold: {cool_threshold}")
print(f"{emoji_count} emojis found in the text. The cool ones are:")
print("\n".join(cool_emojis))