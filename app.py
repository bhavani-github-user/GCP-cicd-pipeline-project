from flask import Flask, render_template, request, redirect

app = Flask(__name__)
suggestions = []

@app.route('/')
def index():
    return render_template('index.html', suggestions=suggestions)

@app.route('/submit', methods=['POST'])
def submit():
    suggestion = request.form['suggestion']
    if suggestion:
        suggestions.append(suggestion)
    return redirect('/')
