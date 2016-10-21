#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Content-type: text/html\n\n"
print '<meta charset="utf-8">'
print "<html>controlador: Error 404!</html>"
try:
	import os
	import sys
	sys.path.append("../../config")
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
	print newRoot
	config.custom_url=newRoot
	if config.mod_debug==False:
		#es una aplicacion ejemp: http://localhost:8000/webpyzer/welcome/default/
		if newRoot[2] in config.apps:
			if newRoot[2]!="admin":
				if len(newRoot)==5:
					print("Location:"+config.host+newRoot[2]+"/0/"+newRoot[3]+"/"+newRoot[4])
					print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+newRoot[2]+'/0/'+newRoot[3]+'/'+newRoot[4]+'/">'

				elif len(newRoot)==4:
					if newRoot[3]!="":
						print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+newRoot[2]+'/0/'+newRoot[3]+'/index/">'
					else:
						print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+newRoot[2]+'/0/default/index/">'
				elif len(newRoot)==3:
					print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+newRoot[2]+'/0/default/index/">'
				
				
			else:
				#print("Location:"+config.host+newRoot[2]+"/produccion/default/index")
				print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+newRoot[2]+'/0/default/index/">'
		else:
			
	
			#es el controlador ejemp:  http://localhost:8000/webpyzer/welcome/default/vista
			if newRoot[2] in config.proyectos:
				if newRoot[2]!="admin" and newRoot[2] in config.proyectos_disp:
					#en el formato proyecto/version/controlador/vista
					print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+newRoot[2]+'/0/default/index/">'
				else:
					"El acceso a este proyecto no esta disponible"
			else:
				print "<h1>La aplicación: '"+newRoot[2]+"'</h1><p>No se encuentra en el nuestras apps en desarrollo</p>"

			
			
	else:
		#si esta el modo programador habilitado
		#es una aplicacion ejemp: http://localhost:8000/webpyzer/welcome/version/default/
		#nota es el acceso version actual del proyecto /0/ 
	
		if newRoot[2] in config.proyectos:
				
				if len(newRoot)==6:
					print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+newRoot[2]+'/'+newRoot[3]+'/'+newRoot[4]+'/'+newRoot[5]+'/">'
				elif len(newRoot)==5:
					print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+newRoot[2]+'/'+newRoot[3]+'/'+newRoot[4]+'/index/">'
				elif len(newRoot)==4:
					if newRoot[3]=="":
						print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+newRoot[2]+'/0/default/index/">'
					else:
						print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+newRoot[2]+'/'+newRoot[3]+'/default/index/">'
				elif len(newRoot)==3:
					print '<meta http-equiv="Refresh" content="0;url='+config.host+newRoot[1]+"/"+newRoot[2]+'/0/default/index/">'
				
		else:
			#es el controlador ejemp:  http://localhost:8000/webpyzer/welcome/version/default/vista
			#la estructura del admin es admin/vista
			if newRoot[2]=="admin":
				
				if len(newRoot)==6:
					print("Location: "+config.host+"admin/desarrollo/default/"+newRoot[5])
				else:
					print("Location: "+config.host+"admin/desarrollo/default/index")
			else:
				print "<h1>La aplicación: '"+newRoot[2]+"'</h1><p>No se encuentra en el nuestras apps en desarrollo</p>"
			pass
			
except Exception, ex:
	print "<h1>Hay un error: </h1>"
	print "<p>"+str(ex)+"</p>"

