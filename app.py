from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

# configure api key for gemini

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


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


@app.route("/christmas-ghost/brothers")
def scenario_ghost_brothers():
    return render_template("brothers.html")


@app.route("/christmas-mystery/celebration")
def scenario_mystery_celebration():
    return render_template("celebration.html")


@app.route("/christmas-cake")
def scenario_cake():
    return render_template("cake.html")


@app.route("/christmas-cake/ending")
def scenario_cake_ending():
    return render_template("cake_ending.html")


@app.route("/generate-plot", methods=["POST"])
def generate_plot():
    genre = request.json.get("genre", "comedy")  # Default to comedy

    try:
        # Gemini API call
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            f"Generate a short movie plot "
            f"for a {genre} film "
            f"starring a blonde actress "
            f"called Cate Blanchett and a grandmother,"
            f"Nana Tina, who joins forces with her."
            f"The plot should have a title, that you output as "
            f"Title: Title Name, followed by - on a new line - the plot,"
            f"formatted as Plot: The plot..."
            f"The maximum plot length should be ~10-15 lines",
            stream=True,
        )
        full_response = ""
        for chunk in response:
            full_response += chunk.text

        # Parse response into title and plot
        title = ""
        plot = ""
        if "Title:" in full_response and "Plot:" in full_response:
            parts = full_response.split("Plot:")
            title = parts[0].replace("Title:", "").strip()
            plot = parts[1].strip()

        return jsonify({"title": title, "plot": plot})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
