words_to_find = input().split(", ")
words_to_check = input()
words_filled = [x for x in words_to_find if x in words_to_check]
print(words_filled)
