def emoticon_finder(text):
    result = [text[i]+text[i+1] for i in range(len(text)) if text[i] in ":" and text[i+1] != " "]
    print("\n".join(result))


data = input()
emoticon_finder(data)