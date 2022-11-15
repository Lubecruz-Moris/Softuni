students_dict = {}
number_of_students = int(input())

for students in range(number_of_students):
    student, grade = input().split()
    if student not in students_dict:
        students_dict[student] = []
    students_dict[student].append(float(grade))

for student, grades in students_dict.items():
    formatted_grades = ' '.join(f'{grade:.2f}' for grade in grades)
    avg_grade = sum(grades) / len(grades)
    print(f"{student} -> {formatted_grades} (avg: {avg_grade:.2f})")