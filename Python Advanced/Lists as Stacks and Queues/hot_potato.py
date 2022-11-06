from collections import deque

kids_string = input()
tosses_count = int(input())
kids = deque(kids_string.split(" "))

current_count = 0

while len(kids) > 1:
    current_count += 1
    kid = kids.popleft()
    if current_count < tosses_count:
        kids.append(kid)
    elif current_count == tosses_count:
        current_count = 0
        print(f"Removed {kid}")

print(f"Last is {kids.popleft()}")
print(kids)