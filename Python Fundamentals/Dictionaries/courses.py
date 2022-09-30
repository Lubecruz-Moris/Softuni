courses = {}
while True:
    command = input()
    if command == "end":
        break
    data = command.split(" : ")
    course = data[0]
    student = data[1]

    if course not in courses:
        courses[course] = []
        courses[course].append(student)
    else:
        courses[course].append(student)

for item, material in courses.items():
    print(f"{item}: {len(material)}")
    for students in material:
        print(f"-- {students}")

