from flask import Flask, render_template
from requests import get

app = Flask(__name__)


@app.route('/')
def home_page():
    blog_data = get('https://api.npoint.io/eb6cd8a5d783f501ee7d').json()
    return render_template('index.html', blogs=blog_data)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route('/post/<int:num>')
def post_page(num):
    blog_data = get('https://api.npoint.io/eb6cd8a5d783f501ee7d').json()
    return render_template("post.html", data=blog_data[num-1])


if __name__ == "__main__":
    app.run(debug=True)
