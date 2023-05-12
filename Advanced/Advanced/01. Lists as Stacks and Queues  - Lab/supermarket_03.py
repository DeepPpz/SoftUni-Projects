from collections import deque

queue = deque()

while True:
    person = input()

    if person == "End":
        print(f"{len(queue)} people remaining.")
        exit(0)

    elif person == "Paid":
        while len(queue):
            print(queue.popleft())

    else:
        queue.append(person)
