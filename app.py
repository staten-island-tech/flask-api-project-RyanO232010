from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('q', '').strip().lower()
    url = "https://api.fbi.gov/wanted/v1/list"

    if query:
        url += f"?q={query}"

    response = requests.get(url)
    data = response.json()
    items = data.get("items", [])

    if query:
        filtered_items = []
        for item in items:
            title = (item.get('title') or '').lower()
            aliases = item.get('aliases') or []

            # Ensure aliases is a list of strings
            aliases = [a.lower() for a in aliases if isinstance(a, str)]

            if query in title or any(query in alias for alias in aliases):
                filtered_items.append(item)

        items = filtered_items

    return render_template("index.html", items=items, query=request.args.get('q', ''))

if __name__ == '__main__':
    app.run(debug=True)