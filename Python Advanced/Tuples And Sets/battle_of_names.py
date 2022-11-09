n = int(input())
odd_set = set()
even_set = set()
for row in range(1, n+1):
    name_num = sum([ord(x) for x in input()]) // row
    if name_num % 2 == 0:
        even_set.add(name_num)
    else:
        odd_set.add(name_num)
odd_sum = sum(odd_set)
even_sum = sum(even_set)
if odd_sum == even_sum:

    result = odd_set.union(even_set)
elif odd_sum > even_sum:
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)
print(*result, sep=", ")