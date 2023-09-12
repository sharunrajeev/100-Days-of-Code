from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
from urllib import parse

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
Bootstrap5(app)

# Database
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    year = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


# WTF Forms
class MovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


class MovieEditForm(FlaskForm):
    rating = FloatField("Rating", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField("Submit")


# TMDB Movie search
AuthCode = "Place your auth code"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {AuthCode}",
}


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    movie_list = []
    for i in movies:
        movie_list.append(i[0])
    return render_template("index.html", movies=movie_list)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieForm()
    if request.method == "POST":
        movie_title = request.form["title"]
        movie_title = parse.quote(movie_title)
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"
        response_data = requests.get(url, headers=headers).json()
        return render_template("select.html", movie_list=response_data["results"])
    return render_template("add.html", form=form)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    response_data = requests.get(url, headers=headers).json()
    form = MovieEditForm()
    if request.method == "POST":
        add_data_to_db(response_data, request.form["rating"], request.form["review"])
        return redirect(url_for("home"))
    return render_template(
        "edit.html", form=form, id=id, name=response_data["original_title"]
    )


def add_data_to_db(data, rating, review):
    movie = Movie(
        id=data["id"],
        title=data["original_title"],
        year=data["release_date"].split("-")[0],
        description=data["overview"],
        rating=rating,
        ranking=data["popularity"],
        review=review,
        image_url=f'https://image.tmdb.org/t/p/original/{data["poster_path"]}',
    )
    db.session.add(movie)
    db.session.commit()


@app.route("/delete/<int:id>")
def delete(id):
    item_to_delete = db.session.execute(db.select(Movie).filter_by(id=id)).scalar_one()
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect('/')


@app.route("/update/<int:id>")
def update(id):
    item_to_update = db.get_or_404(Movie, id)
    form = MovieEditForm()
    if request.method == "POST":
        item_to_update.rating = request.form["rating"]
        item_to_update.review = request.form["review"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template(
        "edit.html", form=form, id=id, name=item_to_update.title
    )


if __name__ == "__main__":
    app.run(debug=True)
