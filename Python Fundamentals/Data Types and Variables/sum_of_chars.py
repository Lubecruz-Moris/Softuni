character_count = int(input())
sum = 0
for characters in range(character_count):
    letter = input()
    sum += ord(letter)
print(f"The sum equals: {sum}")