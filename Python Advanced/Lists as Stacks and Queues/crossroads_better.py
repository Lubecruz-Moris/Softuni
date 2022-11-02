from collections import deque
green_light = int(input())
free_window = int(input())
cars = deque()
cars_passed = 0
car_crashed = False
while not car_crashed:
    command = input()
    if command == "END":
        break
    elif command == "green":
        current_green = green_light
        while cars and current_green > 0:
            car = cars.popleft()
            if len(car) <= current_green + free_window:
                cars_passed += 1
            else:
                print("A crash happened!")
                print(f"{car} was hit at {car[current_green - free_window]}.")
                car_crashed = True
                break
            current_green -= len(car)
    else:
        cars.append(command)

if not car_crashed:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")