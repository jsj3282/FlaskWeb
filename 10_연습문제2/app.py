from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route("/")
@app.route("/<int:num>")
def inputTest(num=None):
    return render_template("index.html", num=num)


@app.route("/calculate", methods=["POST"])
def calculate(num=None):
    if request.method == "POST":
        temp = request.form["num"]
    else:
        temp = None
    return redirect(url_for("inputTest", num=temp))


if __name__ == "__main__":
    app.run()
