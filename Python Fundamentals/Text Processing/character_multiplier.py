def multiplication(first, second):
    total = 0
    for i in range(len(first)):
        if i < len(second):
            total += ord(first[i]) * ord(second[i])
        else:
            total += ord(first[i])
    return total


def character_multiplier(first_word, second_word):
    result = 0
    if len(first_word) > len(second_word):
        result = multiplication(first_word, second_word)
    else:
        result = multiplication(second_word, first_word)
    print(result)


d = input().split()
character_multiplier(d[0], d[1])
