number_of_guests = int(input())
vip_guests = set()
regular_guests = set()
guests = {input() for x in range(number_of_guests)}
while True:
    command = input()
    if command == "END":
        break
    if command in guests:
        guests.remove(command)

for guest in guests:
    if guest[0].isdigit():
        vip_guests.add(guest)
    elif guest[0] not in '0123456789':
        regular_guests.add(guest)

print(len(guests))
if vip_guests:
    vip_formatted = '\n'.join(sorted(vip_guests))
    print(vip_formatted)

if regular_guests:
    regular_formatted = '\n'.join(sorted(regular_guests))
    print(regular_formatted)