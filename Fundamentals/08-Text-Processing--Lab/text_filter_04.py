banned_words = input().split(", ")
text = input()

for ban in banned_words:
    text = text.replace(ban, "*" * len(ban))

print(text)
