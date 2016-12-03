#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Content-type: text/html\n\n"
print '<meta charset="utf-8">'
print "<html>controlador: Error 404!</html>"
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
	print newRoot
	print config.host+newRoot[1]+"/"+config.apps_url+newRoot[2]+"/"+"controles/"+newRoot[3]+"/"
	if config.mod_debug==False:
		#es una aplicacion ejemp: http://localhost:8000/AsenZor/app/vista/
		if newRoot[2] in config.apps:
			print("Location:"+config.host+newRoot[1]+"/"+config.apps_url+newRoot[2]+"/"+"controles/"+newRoot[3]+"/"+newRoot[4])
			print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+config.apps_url+newRoot[2]+"/"+"controles/"+newRoot[3]+"/"+newRoot[4]+'/">'
		else:
			pass
	else:
		if newRoot[2] in config.proyectos_disp:
			print("Location:"+config.host+newRoot[1]+"/"+config.apps_url+newRoot[2]+"/"+"controles/"+newRoot[3]+"/"+config.controler_vista)
			config.host+newRoot[1]+"/"+config.projects_url+newRoot[2]+"/"+"controles/"+newRoot[3]+"/"+config.controler_vista
			#print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+config.projects_url+newRoot[2]+"/"+"controles/"+newRoot[3]+"/"+config.controler_vista+'">'
		else:
			print "Pagina no encontrada"

			
except Exception, ex:
	print "<h1>Hay un error: </h1>"
	print "<p>"+str(ex)+"</p>"

