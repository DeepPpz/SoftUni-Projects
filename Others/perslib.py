def input_on_diff_rows():
    list = [int(input()) for x in range(3)]


def input_with_list_comprehension():
    sequence = [int(n) for n in input().split()]


def validate_index(index):
    if 0 <= index < len(list) -1:
        return True


def word_reversing(word):
    for i in range(len(word) -1, -1, -1):
        print(word[i], end='')


def constant_searching_through_list(list_one, list_two, i):
    curr_idx = sum(list_one[i]) % len(list_two)


def front_to_back(list, idx):
    print(list[-idx:])


def delete_from_list(list, i):
    del list[0:i + 1]


def joins():
    print(','.join(list))
    print(' '.join('{:0.2f}'.format(i) for i in list))


def transforming_time(sum_minutes):
    hours = sum_minutes // 60
    minutes = sum_minutes % 60

    if hours > 23:
        hours = hours - 24
        print(f'{hours}:{minutes:02d}')
    else:
        print(f'{hours}:{minutes:02d}')


def check_time_of_code():
    import time
    start = time.time()
    # main()
    end = time.time()
    print(end - start)