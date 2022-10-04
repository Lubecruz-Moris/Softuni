def caesar_cipher(text):
    result = [chr(ord(ch) + 3) for ch in text]
    print("".join(result))


data = input()
caesar_cipher(data)
