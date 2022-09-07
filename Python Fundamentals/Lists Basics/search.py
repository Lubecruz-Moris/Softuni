number = int(input())
key_word = input()
main_list = list()
filtered_list = list()
for words in range(number):
    current_word = input()
    main_list.append(current_word)
    if key_word in current_word:
        filtered_list.append(current_word)
print(main_list)

print(filtered_list)