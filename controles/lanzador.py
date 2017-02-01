#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Content-type: text/html\n\n"
#print "estas en: lanzador<br>"
try:
	#------------------------------------------------
	#HEAD
	import os
	import gestor
	newRoot=os.environ["REQUEST_URI"].replace("?","").split("/")
	parametros_url=newRoot[-1].split("&")
	parametros_rest={}
	if "&" in newRoot[-1]:
				for elem in parametros_url:
					a=elem.split("=")
					parametros_rest[a[0]]=a[1]
	if "vista=" not in newRoot[-1]:
			  		parametros_rest["vista"]="index"
	if "app=" not in newRoot[-1]:
			  		parametros_rest["app"]="default"
			  	
	
	gestor.administrar(parametros_rest)

except Exception, ex:
	print "<h1>Hay un error3: </h1>"
	print "<p>"+str(Exception)[1:-1]+"</p>"
	print "<p>"+str(ex)+"</p>"