def count_win(symbol, part):
    win_counter = 0
    for s in part:
        if s == symbol:
            win_counter += 1
        elif s != symbol and win_counter > 0:
            return win_counter
    return win_counter


tickets = [x.strip() for x in input().split(',')]
winning_symbols = ["@", "#", "$", "^"]
win, jackpot = False, False

for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue

    first_part = ticket[:10]
    second_part = ticket[10:]

    for sw in winning_symbols:
        if (sw * 6) in first_part and (sw * 6) in second_part:
            counter_first = count_win(sw, first_part)
            counter_second = count_win(sw, second_part)
            counter = min(counter_first, counter_second)
            win = True
            break

    for sj in winning_symbols:
        if (sj * 10) in first_part and (sj * 10) in second_part:
            win = False
            jackpot = True
            break

    if win:
        print(f'ticket "{ticket}" - {counter}{sw}')
        win = False
    elif jackpot:
        print(f'ticket "{ticket}" - 10{sj} Jackpot!')
        jackpot = False
    else:
        print(f'ticket "{ticket}" - no match')
