from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)
from secrets import token_hex

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key-goes-here"

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy()
db.init_app(app)

# Flask Login
app.config[
    "SECRET_KEY"
] = "d4d887e4039210f1ccc977789c9aa29117bec43e7df7cd68f6749b8e85dcc52d"
login_manager = LoginManager()
login_manager.init_app(app=app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def is_authenticated(self):
        return


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        user_data = db.session.execute(
            db.select(User).where(User.email == email)
        ).scalar()
        if user_data:
            flash("User already exist with the email. Try logging in.")
        else:
            user = User(
                name=request.form["name"],
                email=email,
                password=generate_password_hash(
                    password=request.form["password"],
                    method="pbkdf2:sha256",
                    salt_length=8,
                ),
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("secrets"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("secrets"))
            else:
                flash("Incorrect password! Check your password again.")
        else:
            flash("Email not found! Register a new account.")
    return render_template("login.html")


@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
def download():
    if current_user.is_authenticated:
        return send_from_directory(directory="static", path="files/cheat_sheet.pdf")
    else:
        return f"<h1>Unauthorised Access!</h1><p>Try to <a href={url_for('login')}>login</a> to use the service.</p>"


if __name__ == "__main__":
    app.run(debug=True)
