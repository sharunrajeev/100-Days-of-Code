from flask import Flask, render_template, request

app = Flask("FormApp")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        print(name, password)
        return '<h1>Welcome</h1>'
    return '<h1>Error occured</h1>'

app.run(debug=True)