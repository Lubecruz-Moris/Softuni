number_of_students = int(input())
students_dict = {}

for _ in range(number_of_students):
    student = input()
    grade = float(input())
    if student not in students_dict:
        students_dict[student] = []
        students_dict[student].append(grade)
    else:
        students_dict[student].append(grade)

for item, material in students_dict.items():
    average_grade = sum(material) / len(material)
    if average_grade >= 4.5:
        print(f"{item} -> {average_grade:.2f}")
