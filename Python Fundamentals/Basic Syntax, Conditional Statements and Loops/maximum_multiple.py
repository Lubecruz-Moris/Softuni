divisor = int(input())
boundary = int(input())
highest_number = 0
for numbers in range(boundary + 1):
    if numbers % divisor == 0:
       highest_number = numbers
print(highest_number)