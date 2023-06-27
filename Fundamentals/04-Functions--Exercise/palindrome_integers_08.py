def check_palindrome_integers(a):
    for i in range(len(a)):
        curr_int = a[i]
        reversed_int = ''

        for j in range(len(curr_int) - 1, - 1, - 1):
            reversed_int += curr_int[j]

        if curr_int == reversed_int:
            print('True')
        else:
            print('False')


int_sequence = input().split(', ')

check_palindrome_integers(int_sequence)
