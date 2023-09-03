from flask import Flask, render_template, request
import requests
from smtplib import SMTPException, SMTP

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", message="Contact Me")
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name, email, phone, message)
        return render_template("contact.html", message="Message sent successfully!")


def send_email(name, email, phone, message):
    email_message = f"Subject:Message from {name}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\n Message: {message}"
    with SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login('Your Mail', 'Your Password')
        conn.sendmail('Your Mail', email, email_message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
