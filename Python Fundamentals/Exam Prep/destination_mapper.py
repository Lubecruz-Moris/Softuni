import re

text = input()
pattern = r'([/=])([A-Z][A-Za-z]{2,})\1'
points = 0
destinations_list = []
result = re.finditer(pattern, text)
for match in result:
    destination = match.group(2)
    points += len(destination)
    destinations_list.append(destination)
destinations = ", ".join(destinations_list)
print(f'Destinations: {destinations}')
print(f"Travel Points: {points}")