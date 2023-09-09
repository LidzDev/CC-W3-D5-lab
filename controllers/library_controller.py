from flask import render_template, Blueprint, request, redirect
from models.library import books, add_new_book, delete_book, find_book, checkout_book
from models.book import Book

library_blueprint = Blueprint("library", __name__)

@library_blueprint.route("/library")
def index():
    return render_template("index.jinja", title="Lydia's Library", books=books)

@library_blueprint.route("/library", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    isbn = request.form["isbn"]
    new_book = Book(title, author, genre, isbn)
    add_new_book(new_book)
    return redirect("/library")

@library_blueprint.route("/library/<isbn>")
def show_isbn(isbn):
    specific_book = None
    specific_book = find_book(isbn)
    title = "Unfortunately isbn " + isbn + " is unavailable."
    if specific_book: 
        title = "Details for " + specific_book.title
    return render_template("isbn.jinja", title = title, isbn = isbn, book = specific_book)

@library_blueprint.route("/library/<isbn>", methods=["POST"])
def check_out_isbn(isbn):
    checkout_book(isbn)
    return redirect("/library") 

@library_blueprint.route("/library/delete/<isbn>", methods=["POST"])
def delete(isbn):
    delete_book(isbn)
    return redirect("/library")                         