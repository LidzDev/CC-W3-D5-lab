from models.book import Book

book1 = Book("Programming Perl", "Larry Wall", "Programming", "9780596004927")
book2 = Book("Unix Power Tools", "Jerry Peek", "Programming", "9780679790730" )
book3 = Book("Mastering Regular Expressions", "Jeffrey Friedl", "Programming", "9781565922570")

books = (book1, book2, book3)

def list_all_books(books):
    pass

def add_new_book(book):
    books.append(book)

def delete_book():
    pass