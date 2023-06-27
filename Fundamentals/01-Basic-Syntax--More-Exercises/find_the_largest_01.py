number = input()

num_list = list(number)
max_num = ''

while len(num_list) > 0:
    num = max(num_list)
    max_num += num
    num_list.remove(num)

print(max_num)
