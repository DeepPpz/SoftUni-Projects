shopping_list = input().split("!")

while True:
    command = input().split()
    action = command[0]

    if action == "Go":
        print(', '.join(shopping_list))
        exit(0)

    item = command[1]

    if action == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)

    elif action == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)

    elif action == "Correct":
        new_name = command[2]
        if item in shopping_list:
            idx = shopping_list.index(item)
            shopping_list.insert(idx, new_name)
            shopping_list.remove(item)

    elif action == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
