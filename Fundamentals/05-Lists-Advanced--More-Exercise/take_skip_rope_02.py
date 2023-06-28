init_string = input()

numbers_list = [int(x) for x in init_string if x.isdigit()]
symbols_list = [x for x in init_string if not x.isdigit()]

take_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 != 0]

hidden_message = ""

for i in range(len(take_list)):
    m = take_list[i]
    n = skip_list[i]

    if m > 0:
        for _ in range(m):
            if not symbols_list:
                break
            hidden_message += symbols_list[0]
            symbols_list.pop(0)

    if n > 0:
        for _ in range(n):
            if not symbols_list:
                break
            symbols_list.pop(0)

print(hidden_message)
