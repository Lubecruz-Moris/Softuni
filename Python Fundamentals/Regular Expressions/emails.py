import re
text = input()
user_pattern = r'\b(^|(?<=\s))([A-Za-z0-9])+[-._]?[A-Za-z0-9]+\b'
host_pattern = r'\b@?([A-Za-z0-9]+)([.]|[-])?[A-Za-z0-9]+(\.[A-Za-z0-9]+)+'
pattern = rf"{user_pattern}{host_pattern}"

result = re.finditer(pattern, text)
output = list()
for match in result:
    output.append(match.group())

print('\n'.join(output))
