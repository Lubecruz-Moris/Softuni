from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
papers = [int(x) for x in input().split(", ")]
box_num = 50
boxes_filled = 0
while eggs and papers:
    egg = eggs.popleft()
    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    if egg <= 0:
        continue
    paper = papers.pop()
    wrapped_egg = egg + paper
    if wrapped_egg <= box_num:
        boxes_filled += 1
    elif wrapped_egg > box_num:
        continue

if boxes_filled != 0:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    str_eggs = [str(x) for x in eggs]
    print(f"Eggs left: {', '.join(str_eggs)}")
if papers:
    str_papers = [str(x) for x in papers]
    print(f"Pieces of paper left: {', '.join(str_papers)}")
