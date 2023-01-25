from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        vowels = {'a', 'e', 'u', 'i', 'o'}
        result = function()
        return [el for el in result if el.lower() in vowels]


    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
