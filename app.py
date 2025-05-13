from flask import Flask, render_template, request
import requests

app = Flask(__name__) 
"""

@app.route('/', methods=["GET", "POST"])
def home():
    characters = []
    radical_number = None

    if request.method == "POST":
        radical_number = request.form.get("radical")

        url = f"http://ccdb.hemiola.com/characters/radicals/{radical_number}"

        response = requests.get(url)

        if response.status_code == 200:
            characters = response.json()
        else:
            characters = ["Error fetching data"]
            print("Status code:", response.status_code)

    return render_template("index.html", characters=characters, radical_number=radical_number)

 """

@app.route('/', methods=["GET", "POST"])
def home():
    characters = []
    radical_number = None

    if request.method == "POST":
        radical_number = request.form.get("radical")
        print("User entered radical:", radical_number)  # Debug

        # Make sure it's not empty or None
        if radical_number:
            url = f"http://ccdb.hemiola.com/characters/radicals/{radical_number}"
            print("Requesting URL:", url)  # Debug

            response = requests.get(url)
            print("Status code:", response.status_code)  # Debug

            if response.status_code == 200:
                characters = response.json()
            else:
                characters = ["Error fetching data"]
        else:
            characters = ["No radical number provided!"]

    return render_template("index.html", characters=characters, radical_number=radical_number)
