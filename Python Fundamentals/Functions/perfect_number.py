def perfect_number(number):
    divisors_list = list()
    for num in range(1, number + 1):
        if number % num == 0:
            divisors_list.append(num)
    result = sum(divisors_list)
    if result / 2 == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


current_number = int(input())
print(perfect_number(current_number))
