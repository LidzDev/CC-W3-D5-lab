from models.book import Book

book1 = Book("Programming Perl", "Larry Wall", "Programming", "9780596004927")
book2 = Book("Unix Power Tools", "Jerry Peek", "Programming", "9780679790730" )
book3 = Book("Mastering Regular Expressions", "Jeffrey Friedl", "Programming", "9781565922570")
book4 = Book("Hunter's Oath", "Michelle West", "Fantasy", "9780886776817")
book5 = Book("Empire & Ecolitan", "L.E. Modesitt, Jr.", "Science Fiction", "0312878796")

books = [book1, book2, book3, book4, book5]

def add_new_book(book):
    books.append(book)

def delete_book(isbn):
    book_to_delete = find_book(isbn)
    if book_to_delete: books.remove(book_to_delete)

def find_book(isbn):
    book_to_find = None
    for book in books:
        if book.isbn == isbn:
            book_to_find = book
            break
    return(book_to_find)

def checkout_book(isbn):
    book_to_checkout = find_book(isbn)
    book_index = books.index(book_to_checkout)
    book_to_checkout.checking_out()
    books[book_index] = book_to_checkout
