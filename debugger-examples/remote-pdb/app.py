from random import choice

from flask import Flask, render_template
app = Flask(__name__)

CHOICES = ["✨", "🎉", "🤖", "🐢", "👍", "🐙", "👋", "👀"]


@app.route("/")
def serve():
    emoji = choice(CHOICES)

    from remote_pdb import RemotePdb; RemotePdb('127.0.0.1', 5555).set_trace()

    return render_template("index.html", emoji=emoji)


if __name__ == "__main__":
    app.run(port=8000)
