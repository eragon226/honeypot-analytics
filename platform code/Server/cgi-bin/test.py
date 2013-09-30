import exiftool
import database
import hashlib

con = database.setup()

files = "npp.6.4.5.Installer.exe"
f = open(files, 'r')
md5 = hashlib.md5(f.read()).hexdigest()
with exiftool.ExifTool() as et:
    metadata = et.get_metadata(files)
    entry = (md5,
    	metadata['File:FileSize'],
    	metadata['File:FileModifyDate'],
    	metadata['File:FileType'],
    	metadata['File:MIMEType'])
database.add(con,entry)
print entry