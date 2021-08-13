import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# connect too database
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# brings us to the home page / review page
@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


# allows user to search for reviews within the site
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("reviews.html", reviews=reviews)


# allows user to register a profile
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks for existing user
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("We're sorry! This username is already in use.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Congratulations, you're registered!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # checks hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # lets user know that either the password or username is incorrect
                flash("Sorry! That's the incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Sorry! That's the incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# removes user from session cookie
@app.route("/logout")
def logout():
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


# allows user to add a review to site/db
@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "game_name": request.form.get("game_name"),
            "game_review": request.form.get("game_review"),
            "game_price": request.form.get("game_price"),
            "game_rating": request.form.get("game_rating"),
            "reviewed_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Your Review has been added!")
        return redirect(url_for("get_reviews"))
    return render_template("add_review.html")


# users may edit their own reviews
@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "game_name": request.form.get("game_name"),
            "game_review": request.form.get("game_review"),
            "game_price": request.form.get("game_price"),
            "game_rating": request.form.get("game_rating"),
            "reviewed_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Your Review has been updated!")
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    games = mongo.db.games.find().sort("game_name", 1)
    return render_template("edit_review.html", review=review, games=games)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Your review has been deleted!")
    return redirect(url_for("get_reviews"))


@app.route("/get_mangreviews")
def get_mangreviews():
    reviews = list(mongo.db.reviews.find().sort("game_name"))
    return render_template("mang_reviews.html", mang_reviews=reviews)


@app.errorhandler(404)
def error404(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
