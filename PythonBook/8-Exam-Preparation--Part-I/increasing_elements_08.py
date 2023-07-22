n = int(input())
prev_num = curr_line = longest_line = 0

for i in range(n):
    curr_num = int(input())

    if curr_num > prev_num:
        curr_line += 1
    else:
        if curr_line > longest_line:
            longest_line = curr_line
        curr_line = 1

    prev_num = curr_num

if curr_line > longest_line:
    longest_line = curr_line

print(longest_line)
