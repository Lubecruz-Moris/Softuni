from collections import deque
expression = deque(input().split())

main_colors = {'red', 'yellow', 'blue'}
secondary_colors = {'orange', 'purple', 'green'}
found_colors = []
while expression:
    first = expression.popleft()
    second = expression.pop() if expression else ""
    result = first + second
    if result in main_colors or result in secondary_colors:
        found_colors.append(result)
        continue
    result = second + first
    if result in main_colors or result in secondary_colors:
        found_colors.append(result)
        continue
    first = first[:-1]
    second = second[:-1]
    if first:
        expression.insert(len(expression) // 2, first)
    if second:
        expression.insert(len(expression) // 2, second)

result = []
color_matching = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}
for color in found_colors:
    if color in main_colors:
        result.append(color)
        continue
    iscollected = True
    for helper_color in color_matching[color]:
        if helper_color not in found_colors:
            iscollected = False
            break
    if iscollected:
        result.append(color)
print(result)
