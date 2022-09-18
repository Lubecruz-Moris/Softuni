def next_version(version_number):
    version_number = int("".join(version_number)) + 1
    result = [str(num) for num in str(version_number)]
    return ".".join(result)


current_version = input().split(".")
print(next_version(current_version))