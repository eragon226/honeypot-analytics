#!/usr/bin/python
import sys
import cgi
import hashlib
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import exiftool
import database
import fileTool

filedir = "./binaries"

def printHeader():
    print "content-type: text/html\n\n"

form = cgi.FieldStorage()
if not form:
    sys.exit()
    
(data, filename) = fileTool.getFile(form, "upfile")

printHeader()

# error if there's no file
if not data or not filename:      
    sys.exit()
con = database.connect()
md5 =  hashlib.md5(data).hexdigest()
# if the file already exists, we don't want it again
if fileTool.fileExists(data):
    sys.exit()
else:
    fileTool.storeFile(data)
    with exiftool.ExifTool() as et:
    metadata = et.get_metadata(getFileName(data))
    entry = (md5,
        metadata['File:FileSize'],
        metadata['File:FileModifyDate'],
        metadata['File:FileType'],
        metadata['File:MIMEType'])
    database.add(con,entry)

