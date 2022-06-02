from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


class FileForm(FlaskForm):
    files = FileField(validators=[FileRequired("업로드할 파일을 넣어주세요")])


@app.route("/", methods=["GET", "POST"])
def upload_page():
    currentPath = os.getcwd()
    form = FileForm()
    if form.validate_on_submit():
        f = form.files.data
        f.save(
            currentPath
            + "/13_FileServer_validate/uploads/"
            + secure_filename(f.filename)
        )
        return render_template("check.html")
    return render_template("upload.html", form=form)


if __name__ == "__main__":
    # 서버 실행
    app.run()
