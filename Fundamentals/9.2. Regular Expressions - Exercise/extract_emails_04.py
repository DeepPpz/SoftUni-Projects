import re

data = input()

pattern = r"(^|(?<=\s))(?P<user>[a-z]([\.,_-]?[a-z0-9])+)@(?P<host>[a-z-]+\.[a-z-]+(\.[a-z]+)*)"
emails = re.finditer(pattern, data)

for e in emails:
    print(e.group())
