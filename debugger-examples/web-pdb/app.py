from random import choice

from flask import Flask, render_template
app = Flask(__name__)

CHOICES = ["✨", "🎉", "🤖", "🐢", "👍", "🐙", "👋", "👀"]


@app.route("/")
def serve():
    emoji = choice(CHOICES)

    import web_pdb; web_pdb.set_trace()

    return render_template("index.html", emoji=emoji)


if __name__ == "__main__":
    app.run(port=8000)
