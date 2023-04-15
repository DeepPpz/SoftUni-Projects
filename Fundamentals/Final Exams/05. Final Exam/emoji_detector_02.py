import re
emoji_pattern = r"(::|\*\*)[A-Z][a-z]{2,}\1"

data = input()

# cool_threshold = math.prod([int(x) for x in data if x.isdigit()])
cool_threshold = 1
for ch in data:
    if ch.isdigit():
        cool_threshold *= int(ch)

emoji_counter = 0
cool_emojis = []
emojis = re.finditer(emoji_pattern, data)

for emoji in emojis:
    emoji_counter += 1
    curr_emoji = str(emoji.group())
    coolness = 0
    for l in curr_emoji:
        if l not in [":", "*"]:
            coolness += ord(l)

    if coolness >= cool_threshold:
        cool_emojis.append(curr_emoji)

print(f"Cool threshold: {cool_threshold}")
print(f"{emoji_counter} emojis found in the text. The cool ones are:")
print(*cool_emojis, sep="\n")
