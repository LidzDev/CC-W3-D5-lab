class Book:

    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.checked_out = False

    def checking_out(self):
        self.checked_out = True
        return self