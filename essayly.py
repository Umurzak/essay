import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    now= datetime.datetime.now()
    return render_template("main code essayly.html", now=now)

@app.route("/<string:name>")
def hello(name):
    return f"Hello, {name}!"
    
if __name__ == "__main__":
    app.run()
