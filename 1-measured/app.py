import time

from flask import Flask, render_template
app = Flask(__name__)

UPDATE_TIME = 'N/A'


def get_update_time_secs() -> float:
    with open('/app/start-time.txt', 'r') as file:
        start_ns_since_epoch = float(file.read().strip())

    start_secs_since_epoch = start_ns_since_epoch / 10**9
    now_secs_since_epoch = time.time()

    return round(now_secs_since_epoch - start_secs_since_epoch, 2)


@app.route("/")
def serve():
    return render_template("index.html", time=UPDATE_TIME)


if __name__ == "__main__":
    UPDATE_TIME = get_update_time_secs()
    app.run(port=8000)
