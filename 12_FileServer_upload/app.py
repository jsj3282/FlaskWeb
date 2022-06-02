from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #파일 업로드 용량 제한 단위:바이트

# HTML 렌더링
@app.route("/")
def upload_page():
    return render_template("upload.html")


# 파일 업로드 처리
@app.route("/fileUpload", methods=["GET", "POST"])
def upload_file():
    currentPath = os.getcwd()
    if request.method == "POST":
        f = request.files["file"]
        f.save(
            currentPath + "/12_FileServer_upload/uploads/" + secure_filename(f.filename)
        )
        return render_template("check.html")
    else:
        return "Not"


if __name__ == "__main__":
    # 서버 실행
    app.run()
