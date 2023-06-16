from collections import deque

egg_sizes = deque(int(x) for x in input().split(', '))
all_papers = deque(int(x) for x in input().split(', '))
filled_boxes = 0

while egg_sizes and all_papers:
    egg = egg_sizes.popleft()
    paper = all_papers.pop()
    wrapped_egg = egg + paper

    if egg <= 0:
        all_papers.append(paper)
        continue

    if egg == 13:
        all_papers.append(all_papers.popleft())
        all_papers.appendleft(paper)
        continue

    if wrapped_egg <= 50:
        filled_boxes += 1

if filled_boxes > 0:
    print(f'Great! You filled {filled_boxes} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")

if egg_sizes:
    print(f'Eggs left: {", ".join(str(x) for x in egg_sizes)}')
if all_papers:
    print(f'Pieces of paper left: {", ".join(str(x) for x in all_papers)}')
