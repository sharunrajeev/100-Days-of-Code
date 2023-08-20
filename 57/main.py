from flask import Flask, render_template
from datetime import datetime
from requests import get

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.now().year
    return render_template("index.html", year=year)


@app.route('/name/<string:name>')
def name_fn(name):
    age = get(f'https://api.agify.io?name={name}').json()["age"]
    gender = get(f'https://api.genderize.io?name={name}').json()["gender"]
    name = name[0].upper() + name[1:]
    return render_template("index.html", age=age, gender=gender, name=name)


@app.route("/blog")
def blog():
    posts = get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blogs.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
