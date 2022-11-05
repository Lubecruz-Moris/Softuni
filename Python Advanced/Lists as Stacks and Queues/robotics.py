from collections import deque


def hh_mm_ss(time):
    hours = time // 3600 % 60
    minutes = time // 60 % 60
    seconds = time // 1 % 60

    return f'[{hours:02d}:{minutes:02d}:{seconds:02d}]'


def time_calculation(time):

    hours = int(time[0])
    minutes = int(time[1])
    seconds = int(time[2])
    time_in_seconds = int(hours * 3600 / 1 + minutes * 60 / 1 + seconds)
    return time_in_seconds


def item_processing(robots, items, time):
    available_robots = [k for k in robots.keys()]
    working_robots = {}
    while items:
        taken_item = items.popleft()
        time += 1
        if time == 86400:
            time = 0
        for worker in [k for k in working_robots.keys()]:
            working_robots[worker] -= 1
            if working_robots[worker] <= 0:
                working_robots.pop(worker)
        for robot in available_robots:
            if robot not in working_robots:
                working_robots[robot] = robots[robot]
                print(f"{robot} - {taken_item} {hh_mm_ss(time)}")
                break
        else:
            items.append(taken_item)


def factory():
    robots = {}
    info = input().split(";")
    time = input().split(":")
    for i in range(len(info)):
        explode = info[i].split("-")
        robot_name = explode[0]
        processing_time = int(explode[1])
        robots[robot_name] = processing_time
    time_in_seconds = time_calculation(time)
    items = deque()
    while True:
        command = input()
        if command == "End":
            break
        items.append(command)
    item_processing(robots, items, time_in_seconds)


factory()
