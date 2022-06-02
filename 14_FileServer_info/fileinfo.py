import os
import datetime
import time


def stamp2real(stamp):
    return datetime.datetime.fromtimestamp(stamp)


def info(filename):
    ctime = os.path.getctime(filename)  # 만든시간
    mtime = os.path.getmtime(filename)  # 수정시간
    atime = os.path.getatime(filename)  # 마지막 엑세스시간
    size = os.path.getsize(filename)  # 파일크기 (단위: bytes)
    return ctime, mtime, atime, size


currentPath = os.getcwd()
print(currentPath)
filelist = os.listdir(currentPath + "/uploads/")
for name in filelist:
    ctime, mtime, atime, size = info(currentPath + "/uploads/" + name)
    print(name)
    print("생성시간:", stamp2real(ctime))
    print("수정시간:", stamp2real(mtime))
    print("엑세스시간:", stamp2real(atime))

    if size <= 1000000:
        print("%.2f KB\n" % (size / 1024))
    else:
        print("%.2f MB\n" % (size / (1024.0 * 1024.0)))
