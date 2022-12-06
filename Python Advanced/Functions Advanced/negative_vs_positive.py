def negative_positive(*args):
    negative_sum = 0
    positive_sum = 0
    for value in args:
        if value > 0:
            positive_sum += value
        elif value < 0:
            negative_sum += value
    return negative_sum, positive_sum


values = [int(x) for x in input().split()]
negative, positive = negative_positive(*values)
print(negative)
print(positive)
if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
