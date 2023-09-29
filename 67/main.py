from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime as dt

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

# Initialise CKEditor
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


# Configure WTF Tables
class BlogPostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Blog Post Subtitle", validators=[DataRequired()])
    author = StringField("Blog Post Author", validators=[DataRequired()])
    image_url = StringField("Blog Post Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Post Body", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route("/")
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars()
    return render_template("index.html", all_posts=posts)


@app.route("/<int:post_id>")
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        dt_obj = dt.now()
        date_now = (
            dt_obj.strftime("%B")
            + " "
            + dt_obj.strftime("%d")
            + ","
            + dt_obj.strftime("%Y")
        )
        blog_post_data = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            img_url=form.image_url.data,
            body=form.body.data,
            date=date_now,
        )
        db.session.add(blog_post_data)
        db.session.commit()
        return redirect("/")
    return render_template("make-post.html", form=form, heading="New Post")


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    current_blog_data = db.session.execute(
        db.select(BlogPost).filter_by(id=post_id)
    ).scalar()
    form = BlogPostForm(
        title=current_blog_data.title,
        subtitle=current_blog_data.subtitle,
        author=current_blog_data.author,
        image_url=current_blog_data.img_url,
        body=current_blog_data.body,
    )
    if form.validate_on_submit():
        current_blog_data.title = form.title.data
        current_blog_data.subtitle = form.subtitle.data
        current_blog_data.author = form.author.data
        current_blog_data.img_url = form.image_url.data
        current_blog_data.body = form.body.data
        current_blog_data.date = current_blog_data.date
        db.session.commit()
        return redirect("/")
    return render_template("make-post.html", form=form, heading="Edit Post")


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete-post/<int:post_id>", methods=["GET", "POST"])
def delete_post(post_id):
    current_blog_data = db.get_or_404(BlogPost, post_id)
    db.session.delete(current_blog_data)
    db.session.commit()
    return redirect('/')


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
