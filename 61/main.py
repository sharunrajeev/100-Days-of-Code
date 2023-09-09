from flask import Flask, render_template, redirect, request
from forms import login_form
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
app.secret_key = 'thisisasupersecretcode'
bootstrap = Bootstrap4(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = login_form.LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    if form.validate_on_submit():
        print(form.email.data, form.password.data)
        return render_template('success.html')
    else:
        return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
