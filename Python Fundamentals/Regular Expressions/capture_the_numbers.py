import re
result = list()
while True:
    text = input()
    if not text:
        break
    if len(result) == 0:
        result = re.findall(r"\d+", text)
    else:
        result += re.findall(r"\d+", text)

print(" ".join(result))