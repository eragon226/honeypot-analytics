#!/usr/bin/python

import CGIHTTPServer
import BaseHTTPServer
import database

class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

PORT = 9000 

database.setup()

httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
httpd.serve_forever()
