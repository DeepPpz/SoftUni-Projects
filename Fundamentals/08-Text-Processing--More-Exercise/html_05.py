title = input()
content = input()
comment = input()
all_comments = []

while comment != "end of comments":
    all_comments.append(comment)
    comment = input()

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {content}\n</article>")

for com in all_comments:
    print(f"<div>\n    {com}\n</div>")
