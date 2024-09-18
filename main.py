from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "crawler-1"

@app.route("/health")
def hello():
    return "ok"

if __name__ == "__main__":
    app.run()