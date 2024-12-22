from flask import Flask, render_template, url_for

app = Flask(__name__)

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Example storyline route
@app.route("/scenario1")
def scenario1():
    return render_template("scenario1.html")

@app.route("/scenario2")
def scenario2():
    return render_template("scenario2.html")

if __name__ == "__main__":
    app.run(debug=True)