#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Content-type: text/html\n\n"
print '<meta charset="utf-8">'
#print "<html>controlador: Error 404!</html>"
try:
	import os
	import sys
	sys.path.append("../config")
	import config
	newRoot=os.environ['REDIRECT_URL'].split("/")
	#en el formato proyecto/version/controlador/vista
	#si no esta habilitado la gestion de proyectos

	#-------------------------------------------------
	#En "version" se maneja tres parametros:
	# en "produccion" no hay control de versiones
	# =produccion (config.mod_debug == False & este modo indica que se carga las aplicaciones de la carpeta apps)
	# =desarrollo (config.mod_debug == True & este modo solo se usa para el admin)
	# =N (config.mod_debug == True & se administran versiones "N" es un numero)
	#--------------------------------------------------

	config.custom_url=newRoot
	#print newRoot
	
	parametros_url=newRoot[-1].split("&")
	#print newRoot


	
	parametros_rest={}
	
	if newRoot[-1]=="":
		if newRoot[-2]=="admin":
			parametros_rest["admin"]=True
			parametros_rest["vista"]="index"
			parametros_rest["app"]="default"

	else:
		if newRoot[-1]=="admin":
			parametros_rest["admin"]=True
			parametros_rest["vista"]="index"
			parametros_rest["app"]="default"

		else:
			if newRoot[-2]=="admin":
				parametros_rest["admin"]=True			
			if "&" in newRoot[-1]:
				for elem in parametros_url:
					a=elem.split("=")
					parametros_rest[a[0]]=a[1]

			else:

				if "vista=" not in newRoot[-1]:
			  		parametros_rest["vista"]="index"
			  	else:
			  		parametros_rest["vista"]=newRoot[-1].split("=")[1]

			  	if "app=" not in newRoot[-1]:
			  		parametros_rest["app"]="default"
			  	else:
			  		
			  		parametros_rest["app"]=newRoot[-1].split("=")[1]



	notfound=False

	if notfound==False:
		#es una aplicacion ejemp: http://localhost:8000/AsenZor/app/vista/
		import gestor
		gestor.administrar(parametros_rest)

	else:
		print "Pagina no encontrada"

			
except Exception, ex:
	print "<h1>La query enviada tiene un error, por favor utilice parametros validos</h1>"
	if config.mod_debug==False:
		print "<p>"+str(Exception)[1:-1]+"</p>"
		print "<p>"+str(ex)+"</p>"

