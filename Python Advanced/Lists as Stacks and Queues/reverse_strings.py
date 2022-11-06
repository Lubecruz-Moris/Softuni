string = input()
stack = []
for ch in string:
    stack.append(ch)
reverse = ""
while stack:
    reverse += stack.pop()

print(reverse)