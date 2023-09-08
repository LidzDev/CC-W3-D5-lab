from flask import Flask, request
from controllers.library_controller import library_blueprint

app = Flask(__name__)
app.register_blueprint(library_blueprint)