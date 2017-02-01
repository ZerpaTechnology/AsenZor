#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Content-type: text/html\n\n"
import config.config as config
# Import modules for CGI handling 
#siempre debe mandarse action 
try:
	import os
	import commands
	import cgi, cgitb
	import requests
	import httplib, urllib
	import sys
	



	# Create instance of FieldStorage 
	data= cgi.FieldStorage()
	cgitb.enable()
	parametros=os.environ["HTTP_REFERER"].replace("?","&").split("/")[-1].split("&")
	rest={}

	for elem in parametros:

		k,v=elem.split("=")
		rest[k]=v
	if "action" not in data:
		rest["action"]=None
	else:
		rest["action"]=data["action"].value
	sys.path.append(config.base_root+config.apps_url+rest["app"]+"/user/"+config.controles_dir+"/")
	if "vista" not in rest:
		rest["vista"]="index"
	rest["base_root"]=config.base_root+config.apps_url+rest["app"]+"/user/"
	rest["base_url"]=config.base_url+config.apps_url+rest["app"]+"/user/"
	rest["user_ip"]=os.environ["REMOTE_ADDR"] #es la direccion ip del cliente, la cabecera no se puede sobrescribir

	cnt=__import__(config.default_controller.replace(".py",""))

	cnt.action(data,rest)



	#dataURL={}

	#parametros = urllib.urlencode(rest)
	#abrir_conexion = httplib.HTTPConnection("rootcodes.com:80")
	#cabeceras = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	#abrir_conexion.request("POST",config.base_url, parametros, cabeceras)
	#respuesta = abrir_conexion.getresponse()

	#print respuesta.status


	#print '<META HTTP-EQUIV="REFRESH" CONTENT="0;URL=' +config.base_url+config.apps_folder+"app="+data["app"]+config.+"&vista="+data["vista"]'">' 
	# Get data from fields
	#output = data["param"]
	#nota para poder resivir los datos debe ser enviado por post
	#filedata=data["upload"]
	#filedata.file.read()
	# This will print to stdout for testing
	#print("Hello World!!!")
	#print(output)
except Exception, e:
		print "Error en ajax\n"
		print e