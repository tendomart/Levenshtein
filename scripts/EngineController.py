from flask import Flask, render_template

app = Flask(__name__)


# The index page
@app.route("/")
def index():
    return render_template("index.html")


# The login page
@app.route("/login")
def get_login():
    pass


@app.route("/results")
def get_results():
    pass


@app.route("/do_levenshtein_search")
def do_levenshtein_search():
    pass


if __name__ == "__main__":
    app.run(debug=True)
