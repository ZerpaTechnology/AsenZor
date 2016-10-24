#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Content-type: text/html\n\n"
print "Controlador Principal: default<br>"
try:
	#------------------------------------------------
	#HEAD
	import gestor
	gestor.administrar()

except Exception, ex:
	print "<h1>Hay un error: </h1>"
	print "<p>"+str(Exception)+"</p>"
	print "<p>"+str(ex)+"</p>"