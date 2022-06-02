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
    size = os.path.getsize(filename)  # 파일크기 (단위: bytes)
    return ctime, mtime, size


@app.route("/", methods=["GET", "POST"])
def main_page():
    form = FileForm()
    if form.validate_on_submit():
        f = form.files.data
        f.save(
            os.getcwd() + "/15_FileServer_list/uploads/" + secure_filename(f.filename)
        )
        return render_template("check.html", pwd=os.getcwd() + "/uploads")

    filelist = os.listdir(os.getcwd() + "/15_FileServer_list/uploads/")
    infos = []
    for name in filelist:
        fileinfo = {}
        ctime, mtime, size = info(os.getcwd() + "/15_FileServer_list/uploads/" + name)
        fileinfo["name"] = name
        fileinfo["create"] = stamp2real(ctime)
        fileinfo["modify"] = stamp2real(mtime)
        if size <= 1000000:
            fileinfo["size"] = "%.2f KB" % (size / 1024)
        else:
            fileinfo["size"] = "%.2f MB" % (size / (1024.0 * 1024.0))
        infos.append(fileinfo)
    return render_template(
        "home.html",
        form=form,
        pwd=os.getcwd() + "/15_FileServer_list/uploads/",
        infos=infos,
    )


if __name__ == "__main__":
    # 서버 실행
    app.run()
