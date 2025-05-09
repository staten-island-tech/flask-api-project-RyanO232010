from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample movie data
interest = [ 
    {"id": 1, "text": "Damian eats poptarts and begs people for money to get it like a degenerate.", "img": "https://i.pinimg.com/originals/bb/cd/d6/bbcdd6617e163e2fb86b2d52a0ab7e78.jpg"},
    {"id": 2, "text": "Damian likes to play trombone but isn't that good.", "img": "https://bracketfights.com/images/templates/2019/179467/italian-brainrot-bracket-179467/screenshot-2025-04-03-at-40654pmpng.png"},
    {"id": 3, "text": "Damian looks like he would like stuff like this.", "img": "https://i.chzbgr.com/thumb800/40384261/h0A38A25D/funny-memes-dank-memes-memes-meme-funny-tweets-funny-twitter-funny-meme-funny-tumblr-funny-random"}
]

@app.route('/')
def home():
    return render_template('index.html', interest=interest)

if __name__ == '__main__':
    app.run(debug=True) 