vowels = ["a", "o", "u", "e", "i"]
word = input()

no_vowels_list = "".join([ch for ch in word if ch.lower() not in vowels])

print(no_vowels_list)