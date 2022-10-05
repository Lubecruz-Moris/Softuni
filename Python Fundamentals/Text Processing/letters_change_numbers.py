from string import ascii_lowercase
def extract_func(text):
    numbers = [n for n in text if n.isdigit()]
    num = int("".join(numbers))
    result = 0
    for i in range(len(text)):
        if text[i].isalpha():
            index = ascii_lowercase.index(text[i].lower()) + 1
            if i == 0:
                if text[i].islower():
                    result = num * index
                else:
                    result = num / index
            else:
                if text[i].islower():
                    result += index
                else:
                    result -= index
    return result


def letters_change_numbers(data):
    result = 0
    for num in data:
        result += extract_func(num)
    print(f"{result:.2f}")


d = input().split()
letters_change_numbers(d)