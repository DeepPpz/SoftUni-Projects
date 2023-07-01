from typing import Dict
from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available: Dict[str: []] = {}  # author: [books]
        self.rented_books: Dict[str: Dict[str: int]] = {}  # username: {book: days}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}
            return f'{book_name} successfully rented for the next {days_to_return} days!'
        else:
            for books in self.rented_books.values():
                if book_name in books:
                    return f'The book "{book_name}" is already rented and ' \
                           f'will be available in {books[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in self.rented_books[user.username]:
            return f'{user.username} doesn\'t have this book in his/her records!'
        else:
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
