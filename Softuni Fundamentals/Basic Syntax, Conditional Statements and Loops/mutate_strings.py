word_one = input()
word_two = input()
replacement_two = ""
for letters_one in range(1, len(word_one) + 1):
    pass
for letters_two in range(0, len(word_two)):
    replacement_two += word_two[letters_two]
    if replacement_two[letters_two] != word_one[letters_two]:
        print(replacement_two + word_one[letters_two + 1:letters_one])
