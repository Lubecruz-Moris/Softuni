import re
pattern = r"(www\.)([A-Za-z0-9-]+)(\.[a-z]+)+"
output = list()
while True:

    text = input()
    if not text:
        break

    result = re.finditer(pattern, text)
    for match in result:
        output.append(match.group())
print("\n".join(output))
