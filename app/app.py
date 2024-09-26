from flask import Flask, jsonify
from utils import load_and_process_data, search_data  # Ensure this import works

app = Flask(__name__)

# Load data once when the application starts
df = load_and_process_data()


@app.route("/")
def index():
    return "Welcome to the Twitter Data API!"


@app.route("/search/<string:term>", methods=["GET"])
def search(term):
    results = search_data(df, term)
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
