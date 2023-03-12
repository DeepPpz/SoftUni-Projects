text = input()
final_text = ""
expl_power = 0

for i in range(len(text)):
    if text[i] == ">":
        expl_power += int(text[i+1])
        final_text += text[i]
    elif expl_power != 0:
        expl_power -= 1
    else:
        final_text += text[i]

print(final_text)
