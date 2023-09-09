# CodeClan Library Weekend Homework

Your task is to model a Flask app which will list books in a Library.

## MVP

Your application should have a single class - Book - and should contain the following properties:

V * Title
V * Author
V * Genre

Provide the following functionality:

V * List all Books
V * Show an individual Book
V * Add a new Book to the Library.
V * Remove a Book from the Library 
 
V  Draw a diagram showing what happens when a user sends a GET request to `/books`. Where does the request go and how does the server process the request? What files are doing what?
 
## Extensions

V * Add a `checked_out` boolean property to the `Book` class.
V * When displaying a book, display whether it is checked in or checked out.
V * Add some styling using CSS.
V * Add a navigation bar that is shared between all templates

## Advanced Extensions

* Give the user the ability to update whether a book is checked in or out. 
    * Because we can't use the `PUT` HTTP method you will need to use a form to send a `POST` route to `/books/<index>`. This form should use a checkbox or radio buttons to update the checked out status.
* Create a route that displays books of a certain genre using the route`/books/genre/<genre>`.
* Anything else you can think of.

#### Guidance

To style a Flask app you will need to put your CSS files inside a folder called `static` inside the `app` package.

Then add the following line inside the <HEAD> tag of your `base.html`

```html
    <link rel="stylesheet" href="{{ url_for('static', filename='your_file_name.css') }}">
```

> When deleting the Book use a form and the index position of the book to determine which book should be deleted.

> An HTML checkbox input value will only be included in the form dictionary if the box is checked. By default, no value will be present if the checkbox is not checked and the value 'on' will be present if it is checked.

> Grouped Radio buttons need to have the same `name` attribute to allow you to toggle between them.
