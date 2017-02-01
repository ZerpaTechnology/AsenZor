#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler

REDIRECTIONS = {"/slashdot/": "http://slashdot.org/",
                "/freshmeat/": "http://freshmeat.net/"}
LAST_RESORT = "http://google.com/"

class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/controles"]
    def do_HEAD(s):
    	s.send_response(301)
        s.send_header("Location", REDIRECTIONS.get(s.path, LAST_RESORT))
        s.end_headers()

httpd = HTTPServer(("", 8000), Handler)

httpd.serve_forever()