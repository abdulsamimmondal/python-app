from flask import Flask, jsonify
import requests
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/posts')
def posts():
    try:
        response = requests.get(f"{app.config['API_BASE_URL']}/posts")
        posts = response.json()
        return jsonify(posts)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
