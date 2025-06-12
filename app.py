from flask import Flask, render_template, request, redirect, url_for

# include code from my book recommendation py file
from bookrec import *

# ----------------- Flask App Code ----------------- #
app = Flask("__name__")

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/explore")
def input():
    return render_template("input.html")

@app.route("/results", methods=["POST"])
def output():
    recommendations = ""
    title = request.form.get("title", "")
    genre = request.form.get("genre", "")
    recommendations = recommend(title, genre)
    return render_template("output.html", recommendations=recommendations)

'''
# May add in the future but not this time
@app.route('/favorites')
def favorites():
    return render_template('favorites.html')
'''

@app.route('/back')
def back_to_input():
    return redirect(url_for('input'))

if __name__ == '__main__':
    app.run(debug=True)