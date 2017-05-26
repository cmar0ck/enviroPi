#!/usr/bin/python
# coding: utf-8

# Serves files out of its current directory
# Doesn't handle POST request

import SimpleHTTPServer
import SocketServer
import sqlite3 as lite
import socket
import json
import sys

from config import plant_type
from urlparse import urlparse
from time import time

IP = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
PORT = 9091

def dict_factory(cursor, row):
     #Equivalent of the PHP/PDO 'ASSOC' functionality
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

def get_data():
    #Function to be called via URL
	con = lite.connect('assets/db/enviro.db')
	con.row_factory = dict_factory

	with con:

		cur = con.execute('SELECT * FROM ' + plant_type + ' ORDER BY rowid DESC LIMIT 1')
		last_row = cur.fetchone()
		encoded_json = json.dumps(last_row)
				
	return (encoded_json)

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        # Split get request up into components
        req = urlparse(self.path)

        # If requesting for /get_data
        if req.path =='/get_data':
            #This URL will trigger our function and send what it returns back to the browser
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(get_data()) #call  function here
            return

        # Else if requesting /endpoint
        elif req.path == '/endpoint':
            # Print request query
            print req.query
            # Do other stuffs...

        else:
            # serve files, and directory listings by following self.path from current working directory
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.ThreadingTCPServer((IP, PORT),CustomHandler)

print "Server running on:",IP,":",PORT
httpd.serve_forever()
