import re
pattern = r"(?P<title>(?<=<title>).+(?=</title>)).+(?P<content>(?<=<body>).+(?=</body>))"
ignored = r"(<.*?>)|(\\n)"

file = input()

extraction = re.search(pattern, file)
title = extraction.group("title")
content = re.sub(ignored, "", extraction.group("content"))

print(f"Title: {title}")
print(f"Content: {content}")
