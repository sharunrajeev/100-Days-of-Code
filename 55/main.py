# Variable rules
# You can use <variable_name> to create variables in the routes

from flask import Flask
from decorators import *

app = Flask(__name__)


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye Friend"


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"<h2>Hello {name}! You are {number} years old</h2>"


if __name__ == "__main__":
    app.run(debug=True)
    # To start in debug mode use app.run(debug=True)
