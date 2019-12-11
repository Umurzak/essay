import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    now= datetime.datetime.now()
    return render_template("main code essayly.html", now=now)

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    wtype = request.form.get("wtype")
    gender = request.form.get("gender")
    if gender == 'Male':
        gen = "Mr."
    else:
        gen = "Mrs."
    if name == 'Aidar':
        gen = ""
        name = "Sir"
    return render_template("hello.html", name=name, wtype = wtype, gen=gen)
    
if __name__ == "__main__":
    app.run()
