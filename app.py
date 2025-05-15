from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    characters = []
    radical_number = None

    if request.method == "POST":
        radical_number = request.form.get("radical")
        print("User entered radical:", radical_number)

        if radical_number:
            try:
                url = f"http://ccdb.hemiola.com/characters/radicals/{radical_number}"
                print("Requesting URL:", url)
                response = requests.get(url)
                print("Status code:", response.status_code)

                if response.status_code == 200:
                    data = response.json()
                    characters = data.get("characters", [])
                    print("Characters received:", characters)
                else:
                    print(f"Error fetching data: {response.status_code}, {response.text}")
                    characters = [f"Error fetching data (status {response.status_code})"]
            except Exception as e:
                characters = [f"Exception occurred: {str(e)}"]
        else:
            characters = ["No radical number provided!"]

    return render_template("index.html", characters=characters, radical_number=radical_number)

if __name__ == '__main__':
    app.run(debug=True)