"""
URL redirection example.
"""

import BaseHTTPServer
import time
import sys


HOST_NAME = 'localhost' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 80 # Maybe set this to 9000.
REDIRECTIONS = {"/slashdot/": "http://slashdot.org/",
                "/freshmeat/": "http://freshmeat.net/",
                "":"http://localhost/index.py"}
LAST_RESORT = "/"

class RedirectHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(301)
        print "PATH ", s.path 
        s.send_header("Location", REDIRECTIONS.get(s.path, LAST_RESORT))
        s.end_headers()
    def do_GET(s):
        s.do_HEAD()

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), RedirectHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)