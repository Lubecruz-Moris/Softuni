import re

numbers = input()
expression = r'\+359([ -])2\1\d{3}\1\d{4}\b'
output = list()
matches = re.finditer(expression, numbers)
for match in matches:
    output.append(match.group())

print(", ".join(output))