from collections import deque

all_tools = deque(int(x) for x in input().split())
all_substances = deque(int(x) for x in input().split())
all_challenges = [int(x) for x in input().split()]
failed = False

while all_challenges:
    if not all_tools or not all_substances:
        failed = True
        break

    tool = all_tools.popleft()
    substance = all_substances.pop()
    result = tool * substance

    if result in all_challenges:
        all_challenges.remove(result)
    else:
        all_tools.append(tool + 1)
        substance -= 1
        if substance > 0:
            all_substances.append(substance)

if failed:
    print('Harry is lost in the temple. Oblivion awaits him.')
else:
    print('Harry found an ostracon, which is dated to the 6th century BCE.')

if all_tools:
    print(f'Tools: {", ".join(str(x) for x in all_tools)}')
if all_substances:
    print(f'Substances: {", ".join(str(x) for x in all_substances)}')
if all_challenges:
    print(f'Challenges: {", ".join(str(x) for x in all_challenges)}')
