from flask import Flask, render_template

app = Flask(__name__)


# Home route
@app.route("/")
def index():
    return render_template("index.html")


# Example storyline route
@app.route("/start")
def start():
    return render_template("start.html")


@app.route("/christmas-mystery")
def scenario_mystery():
    return render_template("mystery.html")


@app.route("/christmas-mystery/mailbox")
def scenario_mystery_mailbox():
    return render_template("mailbox.html")


@app.route("/christmas-mystery/crossword")
def scenario_mystery_crossword():
    return render_template("crossword.html")


@app.route("/christmas-mystery/confrontation")
def scenario_mystery_confrontation():
    return render_template("confrontation.html")


@app.route("/christmas-mystery/signatures")
def scenario_mystery_signatures():
    return render_template("signatures.html")


@app.route("/christmas-mystery/evilplan")
def scenario_mystery_evilplan():
    return render_template("evilplan.html")


@app.route("/christmas-mystery/stranger")
def scenario_mystery_stranger():
    return render_template("stranger.html")


@app.route("/christmas-mystery/goose")
def scenario_mystery_goose():
    return render_template("goose.html")


@app.route("/christmas-mystery/distracted")
def scenario_mystery_distracted():
    return render_template("distracted.html")


@app.route("/christmas-mystery/earlyconfront")
def scenario_mystery_earlyconfront():
    return render_template("earlyconfront.html")


@app.route("/christmas-ghost")
def scenario_ghost():
    return render_template("ghost.html")


@app.route("/christmas-ghost/refusal")
def scenario_ghost_refusal():
    return render_template("ghostrefusal.html")


@app.route("/christmas-ghost/newspaper")
def scenario_ghost_newspaper():
    return render_template("newspaper.html")


@app.route("/christmas-ghost/memories")
def scenario_ghost_memories():
    return render_template("memories.html")


if __name__ == "__main__":
    app.run(debug=True)
