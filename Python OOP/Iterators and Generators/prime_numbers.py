from math import sqrt
def get_primes(data):
    for num in data:

        if num > 1:
            flag = False
            for i in range(2, int(sqrt(num)) + 1):
                if (num % i) == 0:
                    flag = True
                    break
        if not flag:
            yield num


print(list(get_primes([227, 4, 3, 5, 6, 9, 1, 0])))