from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Всем привет!!!"

# @app.route("/<name>/")
# def index(name:str):
#     return f"Hello {name}!"
