n = int(input())
stack = []

for i in range(n):
    query = input()

    if stack:
        if query == "2":
            stack.pop()
        elif query == "3":
            print(max(stack))
        elif query == "4":
            print(min(stack))

    if query.split()[0] == "1":
        stack.append(query.split()[1])

stack.reverse()

print(*stack, sep=', ')
