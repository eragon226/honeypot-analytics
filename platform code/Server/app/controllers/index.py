import web

view = web.template.render('app/views')

class Index:
	def GET(self):
		web.header("Content-Type","text/html; charset=utf-8")
		return view.index()