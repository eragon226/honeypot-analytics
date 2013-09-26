#!/usr/bin/python
import sys
import cgi
import hashlib
import os

filedir = "./binaries"

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
	md5 = hashlib.md5(data).hexdigest()
    try:
        FILE = open(os.path.join(filedir, md5), "wb")
        FILE.write(data)
        FILE.close()
        return True
    except:
        return False

def fileExists(data):
	md5 = hashlib.md5(data).hexdigest()
    if os.path.isfile(os.path.join(filedir, md5)):
        return True
    return False

def printHeader():
    print "content-type: text/html\n\n"


form = cgi.FieldStorage()
if not form:
    sys.exit()
    
(data, filename) = getFile(form, "upfile")

printHeader()

# error if there's no file
if not data or not filename:      
    sys.exit()
    
# if the file already exists, we don't want it again
if fileExists(data):
    sys.exit()
else:
    storeFile(data)

