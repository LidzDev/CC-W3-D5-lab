from models.book import Book

book1 = Book('Programming Perl', 'Larry Wall', 'Programming')
book2 = Book('Unix Power Tools', 'Jerry Peek', 'Programming')
book3 = Book('Mastering Regular Expressions', 'Jeffrey Friedl', 'Programming')

books = (book1, book2, book3)

def list_all_books(books):
    pass

def add_book(book):
    books.append(book)

def delete_book():
    pass