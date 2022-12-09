from flask import render_template, redirect, request, session
from flask_app import app
# Import models
from flask_app.models import dojo_model as dm


# Home
@app.route("/")
def home():
    return render_template("index.html")


# Post data to db and perform validity check
@app.route("/user_dict", methods=["POST"])
def users():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]

    if not dm.Dojo.validate(request.form):  # Redirect home if NOT True
        return redirect('/')

    # Submit data then display results
    dm.Dojo.add(request.form)
    return redirect("/result")


# Display New User
@app.route("/result")
def results():
    return render_template("results.html")
