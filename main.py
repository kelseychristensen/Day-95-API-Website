from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from get_drink import Drink

app = Flask(__name__)
Bootstrap(app)

drink = Drink()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/spirits")
def spirits():
    return render_template("spirits.html")


@app.route("/random")
def random():
    return render_template("result.html", drink=Drink.get_random)


@app.route("/by-spirit")
def by_spirit(spirit):
    drink_to_gen = Drink.get_by_spirit(spirit)
    return render_template("result.html", drink=drink_to_gen)


if __name__ == '__main__':
    app.run(debug=True)