def grades(number):
    if number < 3:
        return "Fail"
    elif number < 3.5:
        return "Poor"
    elif number < 4.5:
        return "Good"
    elif number < 5.5:
        return "Very Good"
    elif number <= 6:
        return "Excellent"


current_grade = float(input())

print(grades(current_grade))