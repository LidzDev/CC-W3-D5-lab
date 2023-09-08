from flask import render_template, Blueprint
from models.library import books
from models.book import Book

library_blueprint = Blueprint("library", __name__)

@library_blueprint.route("/library")
def index():
    return render_template("index.jinja", title="Lydia's Library", books=books)

@library_blueprint.route("/library/<isbn>")
def show_isbn(isbn):
    title = "Details for " + isbn
    return render_template("isbn.jinja", title = title, isbn = isbn)