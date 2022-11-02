from collections import deque
total_food_quantity = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))
complete_orders = True
while orders:
    if total_food_quantity < orders[0]:
        complete_orders = False
        break
    else:
        current_order = orders.popleft()
        total_food_quantity -= current_order
str_orders = []
while orders:
    str_orders.append(str(orders.popleft()))
if not complete_orders:
    print(f"Orders left: {' '.join(str_orders)}")
else:
    print("Orders complete")

