sequence = input()
symbols, number = "", ""
end_result = ""

for i, char in enumerate(sequence):
    if char.isdigit():
        number += char
        if i + 1 < len(sequence):
            if sequence[i + 1].isdigit():
                continue
        end_result += symbols * int(number)
        symbols, number = "", ""

    else:
        symbols += char

end_result = end_result.upper()
print(f"Unique symbols used: {len(set(end_result))}")
print(end_result)
