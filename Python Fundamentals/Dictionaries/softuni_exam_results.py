submissions_dict = {}
count_dict = {}
while True:
    command = input()
    if command == "exam finished":
        break
    data = command.split("-")
    user = data[0]
    language = data[1]
    if len(data) == 3:
        points = int(data[2])
        if language not in submissions_dict:
            submissions_dict[language] = {}
            submissions_dict[language][user] = points
        elif language in submissions_dict:

            if user in submissions_dict[language]:
                current_points = submissions_dict[language][user]
                if current_points < points:
                    submissions_dict[language][user] = points
            else:
                submissions_dict[language][user] = points
        if language not in count_dict:
            count_dict[language] = 1
        else:
            count_dict[language] += 1

    if language == "banned":
        for languages in submissions_dict:
            for users in submissions_dict[languages]:
                if users == user:
                    submissions_dict[languages][user] = False
print("Results:")
for language in submissions_dict:
    for users in submissions_dict[language]:
        if submissions_dict[language][users]:
            print(f"{users} | {submissions_dict[language][users]}")
print("Submissions:")
for language in count_dict:
    print(f"{language} - {count_dict[language]}")
