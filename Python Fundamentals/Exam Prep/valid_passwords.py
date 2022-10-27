import re
expression = r'^([\W\w]+)>(\d{3,})\|([a-z]{3,})\|([A-Z]{3,})\|([^<>]{3,})<\1$'
count = int(input())
for i in range(count):
    text = input()
    result = re.match(expression, text)
    if result is None:
        print("Try another password!")
    else:
        digits = result.group(2)
        lower = result.group(3)
        upper = result.group(4)
        symbols = result.group(5)
        password = digits + lower + upper + symbols
        print(f"Password: {password}")