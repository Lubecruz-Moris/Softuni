def between_symbols(start, final):
    converted_start = ord(start)
    converted_final = ord(final)
    final_list = []
    for symbol in range(converted_start + 1, converted_final):
        final_list.append(chr(symbol))
    return " ".join(final_list)


symbol1 = input()
symbol2 = input()

print(between_symbols(symbol1, symbol2))

