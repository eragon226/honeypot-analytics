import os
import hashlib
import sys

def getFile(form, key):
    if form.has_key(key):
        item = form[key]
        if item.file and item.filename and item.filename != "":
            data = item.file.read()
            filename = item.filename
            if len(data) > 0:
                return (data, filename)
    return (None, None)

def storeFile(data):
    fileName = getFileName(data)
    try:
        FILE = open(fileName, "wb")
        FILE.write(data)
        FILE.close()
        return True
    except:
        return False

def getFileName(data):
    md5 = hashlib.md5(data).hexdigest()
    return os.path.join(filedir, md5)


def fileExists(data):
	fileName = getFileName(data)
    if os.path.isfile(fileName):
        return True
    return False