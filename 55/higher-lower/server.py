import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='gif'>"


@app.route("/<int:number>")
def check_number(number):
    random_number = random.randint(0, 9)
    if number == random_number:
        return '<h1>Hurray! You won.</h1>'
    else:
        return '<h1>Try again!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
