#!/usr/bin/python

import CGIHTTPServer
import BaseHTTPServer

class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

PORT = 9000 

httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
httpd.serve_forever()
