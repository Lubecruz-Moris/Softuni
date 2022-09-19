words = input().split(" ")
secret_word = input()
palindrome_list = []
word_count = 0
for word in words:
    if word == word[::-1]:
        palindrome_list.append(word)
        if word == secret_word:
            word_count += 1

print(palindrome_list)
print(f"Found palindrome {word_count} times")