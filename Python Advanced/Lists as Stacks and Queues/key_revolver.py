from collections import deque

price_per_bullet = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
intelligence_value = int(input())
bullets_used = 0
present_barrel = gun_barrel_size
while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks[0]
    bullets_used += 1
    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    elif current_bullet > current_lock:
        print("Ping!")
    present_barrel -= 1
    if present_barrel == 0 and len(bullets) > 0:
        print("Reloading!")
        present_barrel = gun_barrel_size
total_earned = intelligence_value - bullets_used * price_per_bullet
if len(bullets) == 0 and len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
elif len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${total_earned}")