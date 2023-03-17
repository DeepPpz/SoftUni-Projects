import re

data = input()

pattern = r"\+359\s2\s[0-9][0-9][0-9]\s[0-9][0-9][0-9][0-9]|\+359-2-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]\b"
phones = re.findall(pattern, data)
print(*phones, sep=", ")
