def odd_even_sum(numbers):
    even_sum = 0
    odd_sum = 0
    for number in numbers:
        if int(number) % 2 == 0:
            even_sum += int(number)
        else:
            odd_sum += int(number)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


command = input()
odd_even_sum(command)