from flask import render_template, Blueprint
from models.library import books
# from models.book import Book

library_blueprint = Blueprint("library", __name__)

@library_blueprint.route("/library")
def index():
    return render_template("index.jinja", title="Lydia's Library", books=books)

@library_blueprint.route("/library/<isbn>")
def show_isbn(isbn):
    title = "Details for isbn " + isbn
    for book in books:
        if book.isbn == isbn:
         return render_template("isbn.jinja", title = title, isbn = isbn, book = book)
    title = "Unfortunately isbn " + isbn + " is unavailable."
    return render_template("isbn.jinja", title =title, isbn = isbn, book=book)

#  sending in the last book in the for loop, we are not going to use it but jinja is not happy without