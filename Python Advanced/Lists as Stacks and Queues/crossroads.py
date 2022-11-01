from collections import deque

green_light_time = int(input())
free_window = int(input())
before_crossing = deque()
cars_list = deque()
cars_passed = 0
new_car = False
everyone_passed = True
while True:
    command = input()
    if command == "END":
        break
    elif command == "green":
        if before_crossing:
            current_car = before_crossing.popleft()

            for i in range(green_light_time):
                if new_car:
                    current_car = before_crossing.popleft()
                current_car.pop(0)
                new_car = False
                if len(current_car) == 0:
                    cars_list.popleft()
                    cars_passed += 1
                    if len(before_crossing) > 0:
                        new_car = True
                    else:
                        break
            if new_car:
                new_car = False
            if len(current_car) > 0:
                for f in range(free_window):
                    if len(current_car) > 0:
                        current_car.pop(0)
                    else:
                        break

                if len(current_car) > 0:
                    print("A crash happened!")
                    print(f"{cars_list.popleft()} was hit at {current_car.pop(0)}.")
                    everyone_passed = False
                    break
                else:
                    cars_list.popleft()
                    cars_passed += 1
    else:
        before_crossing.append([s for s in command])
        cars_list.append(command)


if everyone_passed:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
