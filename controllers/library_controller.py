from flask import render_template, Blueprint

library_blueprint = Blueprint("library", __name__)

@library_blueprint.route('/library')
def index():
    return render_template('index.jinja')