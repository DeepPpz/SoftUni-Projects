first_letter = ord(input())
second_letter = ord(input())
skip_letter = ord(input())
total_comb = 0

for a in range(first_letter, second_letter + 1):
    if a != skip_letter:
        for b in range(first_letter, second_letter + 1):
            if b != skip_letter:
                for c in range(first_letter, second_letter + 1):
                    if c != skip_letter:
                        total_comb += 1
                        print(f"{chr(a)}{chr(b)}{chr(c)}", end=' ')

print(total_comb)
