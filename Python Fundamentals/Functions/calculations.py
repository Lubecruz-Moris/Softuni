def calculator(operator, a, b):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)


current_operator = input()
first_number = int(input())
second_number = int(input())

print(calculator(current_operator, first_number, second_number))