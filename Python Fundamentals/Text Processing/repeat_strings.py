command = input().split(" ")
combined = ""
for word in command:

    combined += word * len(word)

print(combined)