n = int(input())

for i in range(n):
    code = int(input())

    if code == 88:
        message = 'Hello'
    elif code == 86:
        message = 'How are you?'
    elif code < 88:
        message = 'GREAT!'
    else:
        message = 'Bye.'

    print(message)
