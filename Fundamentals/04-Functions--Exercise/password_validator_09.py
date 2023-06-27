def validate_password(a):
    digits_num = 0
    length, chars, digits = True, True, True

    if not 6 <= len(a) <= 10:
        length = False
        print('Password must be between 6 and 10 characters')

    for el in a:
        if 48 <= ord(el) <= 57 or 65 <= ord(el) <= 90 or 97 <= ord(el) <= 122:
            continue
        else:
            chars = False
            print('Password must consist only of letters and digits')
            break

    for d in a:
        if 48 <= ord(d) <= 57:
            digits_num += 1
    if digits_num < 2:
        digits = False
        print('Password must have at least 2 digits')

    if length and chars and digits:
        print('Password is valid')


password = input()

validate_password(password)
