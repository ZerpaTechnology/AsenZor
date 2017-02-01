#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Content-type: text/html\n\n"
print "<link rel='stylesheet' type='text/css' href='http://localhost/zerpatec/static/css/ff.css'>"
print '<meta charset="utf-8">'
# Import modules for CGI handling 

import cgi, cgitb
import os
import sys
import time
import commands
sys.path.append("../modulos")
try:
	from ztec.zred import clienteSock
	# Create instance of FieldStorage 
	#data= cgi.FieldStorage()
	#cgitb.enable()
	print "<body class='ff'>"
	print "hola"
	print " <iframe src='http://localhost/zerpatec/test/servidorSock.py' class='width-100p height-10 b-s1'></iframe> "
	
	clienteSock("localhost",9991,"enviar")
	
	

	
	print "</body>"


except Exception as e:					
		print e