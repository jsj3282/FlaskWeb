from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

import os
import datetime
import time

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


class FileForm(FlaskForm):
    files = FileField(validators=[FileRequired("업로드할 파일을 넣어주세요")])


def stamp2real(stamp):
    return datetime.datetime.fromtimestamp(stamp)


def info(filename):
    ctime = os.path.getctime(filename)  # 만든시간
    mtime = os.path.getmtime(filename)  # 수정시간
    atime = os.path.getatime(filename)  # 마지막 엑세스시간
    size = os.path.getsize(filename)  # 파일크기 (단위: bytes)
    return ctime, mtime, atime, size


@app.route("/", methods=["GET", "POST"])
def upload_page():
    currentPath = os.getcwd()
    form = FileForm()
    if form.validate_on_submit():
        f = form.files.data
        f.save(
            currentPath + "/14_FileServer_info/uploads/" + secure_filename(f.filename)
        )
        fileinfo = {}
        ctime, mtime, atime, size = info(
            currentPath + "/14_FileServer_info/uploads/" + f.filename
        )
        fileinfo["create"] = stamp2real(ctime)
        fileinfo["modify"] = stamp2real(mtime)
        fileinfo["access"] = stamp2real(atime)
        if size <= 1000000:
            fileinfo["size"] = "%.2f KB" % (size / 1024)
        else:
            fileinfo["size"] = "%.2f MB" % (size / (1024.0 * 1024.0))

        return render_template("check.html", fileinfo=fileinfo)
    return render_template("upload.html", form=form)


if __name__ == "__main__":
    # 서버 실행
    app.run()
