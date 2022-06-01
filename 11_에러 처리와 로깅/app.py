from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error("Page not found!!!")  # 에러 메시지 남기기
    return render_template("page_not_found.html"), 404


@app.route("/", methods=["GET", "POST"])
@app.route("/user", methods=["GET", "POST"])
def post():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        value = request.form["input"]
        return render_template("welcome.html", name=value)


@app.route("/test")
def test():
    return "<h1>test</h1>"


if __name__ == "__main__":
    app.run(debug=True)
