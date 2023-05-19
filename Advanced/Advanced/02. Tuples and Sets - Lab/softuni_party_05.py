n = int(input())
guest_list = set([input() for i in range(n)])

while True:
    curr_guest = input()

    if curr_guest == "END":
        sorted_guest_list = sorted(guest_list)
        break
    else:
        guest_list.discard(curr_guest)

print(len(guest_list))
print(*sorted_guest_list, sep='\n')
