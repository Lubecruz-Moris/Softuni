def operate(operator, *args):
    def add(*args):
        return sum(args)

    def subtract(x, *args):
        return x + sum(-y for y in args)

    def multiply(x, *args):
        result = x
        for x in args:
            result *= x
        return result

    def divide(x, *args):
        result = x
        for x in args:
            result /= x
        return result

    operations_map = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    return operations_map[operator](*args)


print(operate("+", 1, 2, 3))
print(operate("-", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 3, 4, 5, 2))
