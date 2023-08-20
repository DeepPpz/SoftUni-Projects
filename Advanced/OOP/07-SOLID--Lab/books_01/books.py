class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.curr_page = 0

    @property
    def pages(self):
        return self.__pages
    
    @pages.setter
    def pages(self, value):
        if value <= 0:
            raise ValueError("The total number of pages for the book cannot be 0 or negative!")
        
        self.__pages = value
    
    def go_to_page(self, page: int):
        if page > self.pages or page < 0:
            raise ValueError("Invalid page!")
        self.curr_page = page
    
    def turn_page(self):
        self.curr_page += 1
    
    def get_current_page(self):
        return f"You're on page number {self.curr_page}."
    
    def __repr__(self):
        return f"\"{self.title}\" by {self.author} with {self.pages}"


class Library:
    MAX_BOOKS = 250
    
    def __init__(self, name: str):
        self.name = name
        self.books = []
    
    def add_book(self, book: Book):
        if len(self.books) >= self.MAX_BOOKS:
            raise Exception("Invalid space for more books!")
        
        self.books.append(book)
        return f"Book {book} is added to {self.name}."
    
    def add_book_to_specific_place(self, book: Book, place: int):
        if not 0 < place <= self.MAX_BOOKS:
            raise Exception("Invalid place for book!")
        
        self.books.insert(place, book)
        return f"Book {book} is added to {self.name} at place no. {place}."
    
    def find_book(self, book_title: str):        
        for i in range(len(self.books)):
            if book_title == self.books[i].title:
                return f"{book_title} is at place no.{i + 1}"
        
        return f"{book_title} does not exist in the Library!"
