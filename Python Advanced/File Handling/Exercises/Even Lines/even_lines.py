symbols_to_replace = ["-", ",", ".", "!", "?"]
with open("../text.txt", 'r') as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for symbol in symbols_to_replace:
                result = result.replace(symbol, "@")
            print(result)

