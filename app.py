from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('q', '').strip().lower()
    page = request.args.get('page', 1, type=int)
    
    url = f"https://api.fbi.gov/wanted/v1/list?page={page}"

    if query:
        url += f"&q={query}"

    response = requests.get(url)
    data = response.json()
    items = data.get("items", [])
    total_pages = (data.get("total", 0) // data.get("pageSize", 20)) + 1  # default page size is 20

    if query:
        filtered_items = []
        for item in items:
            title = (item.get('title') or '').lower()
            aliases = item.get('aliases') or []
            aliases = [a.lower() for a in aliases if isinstance(a, str)]
            if query in title or any(query in alias for alias in aliases):
                filtered_items.append(item)
        items = filtered_items

    return render_template(
        "index.html",
        items=items,
        query=request.args.get('q', ''),
        page=page,
        total_pages=total_pages
    )

if __name__ == '__main__':
    app.run(debug=True)


