order_dict = {}
while True:
    command = input()
    if command == "buy":
        break
    command = command.split(" ")
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product in order_dict:
        order_dict[product] = [price, quantity + order_dict[product][1]]
    else:
        order_dict[product] = [price, quantity]

for key in order_dict:
    total = order_dict[key][0] * order_dict[key][1]
    print(f"{key} -> {total:.2f}")
