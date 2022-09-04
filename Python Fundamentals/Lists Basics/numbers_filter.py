count_of_numbers = int(input())
numbers = list()
positive = list()
negative = list()
odd = list()
even = list()

for num in range(count_of_numbers):
    current_number = int(input())
    numbers.append(current_number)

command = input()

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

print(eval(command))