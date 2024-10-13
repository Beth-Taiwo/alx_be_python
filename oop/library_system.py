class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        for book in self.books:
            if book.__class__.__name__ == 'Book':
                print(f"{book.__class__.__name__}: {book.title} by {book.author}")
            elif book.__class__.__name__ == 'EBook':
                print(f"{book.__class__.__name__}: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif book.__class__.__name__ == 'PrintBook':
                print(f"{book.__class__.__name__}: {book.title} by {book.author}, Page Count: {book.page_count}")

