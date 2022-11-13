cars = set()
num = int(input())
for _ in range(num):
    command, car = input().split(", ")
    if command == "IN":
        cars.add(car)
    elif command == 'OUT' and car in cars:
        cars.remove(car)

if not cars:
    print("Parking Lot is Empty")
else:
    print('\n'.join(car for car in cars))