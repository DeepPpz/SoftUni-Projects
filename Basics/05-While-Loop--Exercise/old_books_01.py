wanted_book = input()

checked_books = 0
book_found = False

while True:
    book = input()

    if book != wanted_book:
        if book == 'No More Books':
            break
        else:
            checked_books += 1
        continue
    else:
        book_found = True
        break

if book_found:
    print(f'You checked {checked_books} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {checked_books} books.')
