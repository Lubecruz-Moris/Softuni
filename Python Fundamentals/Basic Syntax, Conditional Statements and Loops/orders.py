number_of_orders = int(input())
total_price = 0
for orders in range(number_of_orders):
    price = float(input())
    days = int(input())
    capsule_count = int(input())
    order_price = price * days * capsule_count
    total_price += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")
print(f"Total: ${total_price:.2f}")