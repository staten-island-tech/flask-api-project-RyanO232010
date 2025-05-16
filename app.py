from flask import Flask, render_template, jsonify
import requests
from flask_cors import CORS  # Importing CORS

app = Flask(__name__)
CORS(app)  # Enabling CORS for all routes

DND_API_URL = "https://www.dnd5eapi.co/api/ability-scores/cha"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/charisma', methods=['GET'])
def get_charisma():
    try:
        response = requests.get(DND_API_URL)
        response.raise_for_status()  # Check for errors
        data = response.json()

        result = {
            "name": data.get("name"),
            "full_name": data.get("full_name"),
            "desc": data.get("desc", []),  # Default to an empty list if no description
            "skills": data.get("skills", [])  # Default to an empty list if no skills
        }
        return jsonify(result)
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch data from D&D API", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)