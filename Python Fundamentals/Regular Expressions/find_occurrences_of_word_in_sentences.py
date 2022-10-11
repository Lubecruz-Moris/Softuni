import re
sentence = input()
special_word = input()
pattern = rf'\b{special_word}\b'

result = re.findall(pattern, sentence, re.I)
print(len(result))