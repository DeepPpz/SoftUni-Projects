start_num = int(input())
end_num = int(input())
possible_symbols = ['a', 'b', 'c', 'd', 'e']
found = False

for first in possible_symbols:
    for second in possible_symbols:
        for third in possible_symbols:
            for forth in possible_symbols:
                for fifth in possible_symbols:
                    curr_comb = first + second + third + forth + fifth
                    valid_letters = first

                    if valid_letters.find(second) == -1:
                        valid_letters += second
                    if valid_letters.find(third) == -1:
                        valid_letters += third
                    if valid_letters.find(forth) == -1:
                        valid_letters += forth
                    if valid_letters.find(fifth) == -1:
                        valid_letters += fifth

                    total_weight = 0
                    for i in range(len(valid_letters)):
                        if valid_letters[i] == "a":
                            total_weight += 5 * (i + 1)
                        elif valid_letters[i] == "b":
                            total_weight += (-12) * (i + 1)
                        elif valid_letters[i] == "c":
                            total_weight += 47 * (i + 1)
                        elif valid_letters[i] == "d":
                            total_weight += 7 * (i + 1)
                        elif valid_letters[i] == "e":
                            total_weight += (-32) * (i + 1)

                    if start_num <= total_weight <= end_num:
                        found = True
                        print(curr_comb, end=' ')
if not found:
    print("No")
