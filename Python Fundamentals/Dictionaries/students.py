courses = {}
command = input()

while ":" in command:
    data = command.split(":")
    student = data[0]
    id = data[1]
    course = data[2].lower()

    if course not in courses.keys():
        courses[course] = dict()

    courses[course][id] = student

    command = input()

command = command.replace("_", " ").lower()


for id in courses[command]:
    print(f"{courses[command][id]} - {id}")
