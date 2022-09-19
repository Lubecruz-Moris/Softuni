number_of_rooms = int(input())
game_on = True
total_chairs = 0
for room in range(1, number_of_rooms + 1):
    command = input()
    chairs_and_visitors = command.split(" ")
    chairs = len(chairs_and_visitors[0])
    visitors = int(chairs_and_visitors[1])
    diff = abs(chairs - visitors)
    if chairs < visitors:
        print(f"{diff} more chairs needed in room {room}")
        game_on = False
    elif chairs > visitors:
        total_chairs += diff
if game_on:
    print(f"Game On, {total_chairs} free chairs left")