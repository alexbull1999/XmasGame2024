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


if __name__ == "__main__":
    app.run(debug=True)
