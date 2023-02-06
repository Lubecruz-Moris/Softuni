def fibonacci():
    first = 0
    second = 1
    while True:
        yield first
        yield second
        first = first + second
        second = first + second


generator = fibonacci()
for i in range(11):
    print(next(generator))
