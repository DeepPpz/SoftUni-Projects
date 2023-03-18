import re

data = input()

pattern = r"\+359\s2\s[0-9]{3}\s[0-9]{4}|\+359-2-[0-9]{3}-[0-9]{4}\b"
phones = re.findall(pattern, data)
print(*phones, sep=", ")
