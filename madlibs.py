"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]

NOUNS = [
"Apple",
"Car",
"Tree",
"Book",
"Dog",
"Cat",
"House",
"Chair",
"Sun",
"Moon",
"Ocean",
"Mountain",
"River",
"Flower",
"Pen",
"Table",
"Laptop",
"Bird",
"Fish",
"Bicycle",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")

@app.route("/goodbye")
def show_goodbye_page():
    return render_template("goodbye.html")

@app.route("/greet")
def greet_person():
    """Greet user and ask if they want to play MadLibs."""

    player = request.args.get("person")
    return render_template("madlibs.html", person= player)

@app.route("/game")
def show_madlib_form():
    player = request.args.get("person")
    wants_to_play_a_game = request.args.get("answer")
    if wants_to_play_a_game == "no":
        return render_template("goodbye.html")
    elif wants_to_play_a_game == "yes":
        return render_template("game.html", person=player)
    
@app.route("/madlib")
def show_madlib():
    color = request.args.get("color")
    # noun1 = request.form.get("noun1")
    # noun2 = request.form.get("noun2")
    # noun3 = request.form.get("noun3")
    adjective = request.args.get("adjective")
    person = request.args.get("person")
    print(f"There once was a {{ color }} {{ noun1 }} sitting in the Hackbright Lab. When {{ person }} went to pick it up, it burst into flames in a totally {{ adjective }} way.")

    return render_template("show_madlib.html", color=color, adjective=adjective, person=person)

   


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
