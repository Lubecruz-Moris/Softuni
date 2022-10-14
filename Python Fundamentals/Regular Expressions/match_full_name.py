import re
names = input()
expression = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(expression, names)
print(" ".join(matches))