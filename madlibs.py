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
    return render_template("compliment.html", person= player)

@app.route("/game")
def show_madlib_form():
    player = request.args.get("person")
    wants_to_play_a_game = request.args.get("answer")
    if wants_to_play_a_game == "no":
        return render_template("goodbye.html")
    elif wants_to_play_a_game == "yes":
        return render_template("compliment.html", person=player)

   


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
