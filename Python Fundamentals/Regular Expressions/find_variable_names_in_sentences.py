import re
text = input()
pattern = r'\b_[A-Za-z0-9]+\b'
result = re.findall(pattern, text)
output = list()
for word in result:
    output.append(word[1:])

print(",".join(output))