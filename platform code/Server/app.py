
import sys
import web
import database
import app.controllers

urls = (
	'/', 'app.controllers.index.Index',
	'/upload/log', 'app.controllers.upload.Log',
	'/upload/sample', 'app.controllers.upload.Sample', 
)

if __name__ == "__main__":
	database.setup()
	app = web.application(urls, globals()) 
	app.run()