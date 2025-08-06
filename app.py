from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "🚀 Flask App with CI/CD via Cloud Build deployed successfully!"

if __name__ == '__main__':
    # ✅ Fix: Use port 8080 and host 0.0.0.0 for Cloud Run compatibility
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
