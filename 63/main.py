from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-book-collection.db"


db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    with app.app_context():
        db.create_all()
    books = db.session.execute(db.select(Book)).scalars()
    print(books)
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(
            title=request.form["name"],
            author=request.form["author"],
            rating=request.form["rating"],
        )
        with app.app_context():
            db.session.add(book)
            db.session.commit()
        return redirect(url_for("home"))
    if request.method == "GET":
        return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    book = db.session.execute(db.select(Book).filter_by(id=id)).scalar()
    if request.method == "POST":
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book)


@app.route("/delete/<int:id>")
def delete(id):
    book = db.session.execute(db.select(Book).filter_by(id=id)).scalar()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
