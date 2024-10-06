class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
        
    def check_out_book(self):
        self._is_checked_out = True
        
    def return_book(self):
        self._is_checked_out = False  # Set book to available again
    
class Library:
    def __init__(self):
        self._books = []
        
    def add_book(self, book):
        self._books.append(book);
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out_book()
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
    
    def list_available_books(self):
        available_books = [f"{book.title} by {book.author}" for book in self._books if not book._is_checked_out]
        print("\n".join(available_books))
        