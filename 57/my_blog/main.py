from flask import Flask, render_template
from requests import get

app = Flask(__name__)


@app.route('/')
def home():
    posts = get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=posts)


@app.route('/post/<int:id>')
def post(id):
    posts = get("https://api.npoint.io/c790b4d5cab58020d391").json()
    for post_item in posts:
        if post_item["id"] == id:
            post_data = post_item
    return render_template("post.html", post=post_data)


if __name__ == "__main__":
    app.run(debug=True)
