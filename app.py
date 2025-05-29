from flask import Flask, render_template, request, redirect, url_for

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("input.html")

@app.route("/explore")
def input():
    return render_template("input.html")

@app.route("/results", methods=["POST"])
def output():
    user_input = request.form.get("desc", "")
    return render_template("output.html", desc=user_input)

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')

@app.route('/back')
def back_to_input():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)