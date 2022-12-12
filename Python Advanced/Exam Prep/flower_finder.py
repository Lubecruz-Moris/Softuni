from collections import deque


def match_letters(v, c, word_set):
    if v in word_set:
        word_set.remove(v)
    if c in word_set:
        word_set.remove(c)


vowels = deque(input().split())
consonants = input().split()

rose = set("rose")
tulip = set("tulip")
lotus = set("lotus")
daffodil = set("daffodil")
word_match = None
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    match_letters(vowel, consonant, rose)
    if not rose:
        word_match = "rose"
        break

    match_letters(vowel, consonant, tulip)
    if not tulip:
        word_match = "tulip"
        break

    match_letters(vowel, consonant, lotus)
    if not lotus:
        word_match = "lotus"
        break

    match_letters(vowel, consonant, daffodil)
    if not daffodil:
        word_match = "daffodil"
        break

if word_match:
    print(f"Word found: {word_match}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")