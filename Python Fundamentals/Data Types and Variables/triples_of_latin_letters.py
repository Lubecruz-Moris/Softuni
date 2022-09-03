num = int(input())
for first in range(0, num):
    for second in range(0, num):
        for third in range(0, num):
            print(f"{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}")