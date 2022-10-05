def extract_file(file):
    file_info = file.split(".")
    name = file_info[0]
    extension = file_info[1]
    return f"""File name: {name}
File extension: {extension}"""


data = input().split("\\")
print(extract_file(data[-1]))