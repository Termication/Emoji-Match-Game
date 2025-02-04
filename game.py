from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)
app.secret_key = "DEFnbjxuhjgHBI12345"

EMOJIS = ["😄", "😂", "🙃", "🥰", "😭", "😍", "😎", "🤔", "🤩", "😡",
          "😴", "😇", "🤯", "🤡", "😬", "🤓", "🥳", "😢", "🤤", "🤑",
          "🥺", "😱", "😷", "🤒", "🤕", "🧐", "😪", "🤪", "🫠", "🥶",
          "😵", "🤠", "👿", "🧛", "🧟", "👽", "👻", "💀", "🎃", "🤖",
          "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯",
          "🦁", "🐮", "🐷", "🐸", "🐵", "🐔", "🐧", "🐦", "🐤", "🦆",
          "🦅", "🦉", "🐴", "🦄", "🐝", "🐛", "🦋", "🐌", "🐞", "🐜",
          "🦟", "🦗", "🕷", "🦂", "🐢", "🐍", "🦎", "🐙", "🦑", "🦀",
          "🐡", "🐠", "🐟", "🐬", "🐳", "🐋", "🦈", "🦧", "🐘", "🦏"]

@app.route('/')
def index():
    return render_template('game.html')

@app.route('/new-round')
def new_round():
    target = random.choice(EMOJIS)
    num_options = min(80, len(EMOJIS))
    options = random.sample(EMOJIS, num_options - 1)
    options.append(target)
    random.shuffle(options)

    return jsonify({"target": target, "options": options})

if __name__ == '__main__':
    app.run(debug=True)
