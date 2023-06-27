voucher = int(input())
total_tickets = 0
total_others = 0

while True:
    purchase = input()

    if purchase == "End" or voucher <= 0:
        break

    if len(purchase) > 8:
        voucher -= ord(purchase[0]) + ord(purchase[1])
        if voucher >= 0:
            total_tickets += 1
        else:
            break

    else:
        voucher -= ord(purchase[0])
        if voucher >= 0:
            total_others += 1
        else:
            break

print(f"{total_tickets}\n{total_others}")
