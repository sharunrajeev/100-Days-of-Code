from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # dict = {}
        # for col in self.__table__.columns:
        #     dict[col.name] = getattr(self, col.name)
        # return dict
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def random():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    cafes = {count: cafe.to_dict() for count, cafe in enumerate(all_cafes)}
    return jsonify(cafes=cafes)


@app.route("/search")
def search():
    loc = request.args.get("loc")
    cafes = (
        db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    )
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return (
            jsonify(
                error={"Not Found": "Sorry, we don't have a cafe at that location."}
            ),
            404,
        )


## HTTP POST - Create Record
@app.post("/add")
def add():
    new_cafe = Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url=request.form["img_url"],
        location=request.form["location"],
        seats=request.form["seats"],
        has_toilet=request.form["has_toilet"],
        has_wifi=request.form["has_wifi"],
        has_sockets=request.form["has_socket"],
        can_take_calls=request.form["can_take_calls"],
        coffee_price=request.form["coffee_price"],
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe data."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return (
            jsonify(
                error={
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }
            ),
            404,
        )


## HTTP DELETE - Delete Record
@app.route("/delete/<id>")
def delete(id):
    if request.args["api-key"] == "TheTopSecretKey":
        cafe = db.get_or_404(Cafe, id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."}), 200
        else:
            return (
                jsonify(
                    error={
                        "Not Found": "Sorry a cafe with that id was not found in the database."
                    }
                ),
                404,
            )
    else:
        return (
            jsonify(
                error={
                    "Invalid API Key": "Your API Key is invalid. Please check and try again."
                }
            ),
            404,
        )


## Functions


if __name__ == "__main__":
    app.run(debug=True)
