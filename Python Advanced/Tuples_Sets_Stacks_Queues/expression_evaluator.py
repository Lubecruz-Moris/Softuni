from collections import deque
expression = input().split()
nums = deque()
operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}
for ch in expression:
    if ch in operators:
        while len(nums) > 1:
            first = nums.popleft()
            second = nums.popleft()
            nums.appendleft(operators[ch](first, second))
    else:
        nums.append(int(ch))
print(nums.popleft())

