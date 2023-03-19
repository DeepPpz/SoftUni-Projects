import re

sentence = input().lower()
word = input().lower()

pattern = rf"\b{word}\b"
#pattern = r"\b" + word + r"\b"
print(len(re.findall(pattern, sentence)))
