from flask import Flask, render_template, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

DND_API_URL = "https://www.dnd5eapi.co/api/ability-scores/"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/abilities', methods=['GET'])
def get_ability_urls():
    try:
        response = requests.get(DND_API_URL)
        response.raise_for_status()
        data = response.json()

        results = data.get("results", [])

        # Build a list of abilities with index, name, and full URL
        abilities = [
            {
                "index": ability.get("index"),
                "name": ability.get("name"),
                "url": f"https://www.dnd5eapi.co{ability.get('url')}"
            }
            for ability in results
        ]

        return jsonify(abilities)

    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch ability scores", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
