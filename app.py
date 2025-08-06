from flask import Flask, render_template, request

app = Flask(__name__)
suggestions = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        suggestion = request.form.get("suggestion")
        if suggestion:
            suggestions.append(suggestion)
    return render_template("index.html", suggestions=suggestions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
