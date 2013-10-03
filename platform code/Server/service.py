#!/usr/bin/python
import web
import database
import os
import hashlib
import sys
import exiftool

urls = (
	'/', 'Index',
	'upload/log', 'Log',
	'/upload/sample', 'Sample', 
)

class Index:
	def GET(self):
		web.header("Content-Type","text/html; charset=utf-8")
		return """<html>
		<head></head>
		<body> Hello World </body>
		</html>"""

class Log:
	def GET(self):
		web.header("Content-Type","text/html; charset=utf-8")
		return """<html><head></head><body>
		<form method="POST" enctype="multipart/form-data" action="">
		<input type="file" name="myfile" />
		<br/>
		<input type="submit" />
		</form>
		</body></html>"""

	def POST(self):
		x = web.input(myfile={})
		filedir = 'uploads/logs' # change this to the directory you want to store the file in.
		if 'myfile' in x: # to check if the file-object is created
			filename=hashlib.md5(x.myfile.filename).hexdigest()
			if fileExists(filedir + "/" + filename):
				raise web.seeother('/upload/log')
			else:
				fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
				fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
				fout.close() # closes the file, upload complete.
		raise web.seeother('/upload/log')

class Sample:
	def GET(self):
		web.header("Content-Type","text/html; charset=utf-8")
		return """<html><head></head><body>
		<form method="POST" enctype="multipart/form-data" action="">
		<input type="file" name="myfile" />
		<br/>
		<input type="submit" />
		</form>
		</body></html>"""

	def POST(self):
		x = web.input(myfile={})
		filedir = 'uploads/samples' # change this to the directory you want to store the file in.
		con = database.connect()
		if 'myfile' in x: # to check if the file-object is created
			filename=hashlib.md5(x.myfile.filename).hexdigest()
			if fileExists(filedir + "/" + filename):
				raise web.seeother('/upload/sample')
			else:
				fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
				fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
				fout.close() # closes the file, upload complete.
				with exiftool.ExifTool() as et:
					metadata = et.get_metadata(filedir + '/' + filename)
					web.debug(metadata)
					entry = (filename,
						metadata['File:FileSize'],
						metadata['File:FileModifyDate'],
						metadata['File:FileType'],
						metadata['File:MIMEType'])
					database.add(con,entry)
			raise web.seeother('/upload/sample')


def fileExists(fullPath):
	if os.path.isfile(fullPath):
		return True
	return False

if __name__ == "__main__":
	database.setup()
	app = web.application(urls, globals()) 
	app.run()