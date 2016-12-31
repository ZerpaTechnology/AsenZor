#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
	#------------------------------------------------
	#HEAD
	import cgi
	import os
	import time
	import sys
	import httplib, urllib, urllib2, cookielib

	import shutil
	sys.path.append("../config")
	import config
	sys.path.append(config.main_libs_url_relative)
	lista="{"
	for elem in dir(config):
		if elem != "__builtins__" and elem != "__doc__" and  elem != "__file__" and elem != "__name__" and elem != "__package__":
			exec("temp=config."+elem)
			temp=str(temp)
			if temp[0]=="[" or temp[0]=="{":
				lista+= '"'+elem+'":'+temp.replace("'",'"')+',\n'
			elif temp.replace(" ","")=="False,":
				temp="false,"
			elif temp.replace(" ","")=="True":
				temp="true,"
			else:
				lista+= '"'+elem+'":"'+temp+'",\n'

	lista=lista[:-2]+"}"
	f=open(config.base_root+"config/config.json","w")
	lista=lista.encode("base64")
	f.write(lista)
	f.close()
		
	for elem in config.libs:
		exec("import "+elem)

	
	def generar(ruta_html,ruta_python,cabecera):
		import ztec.intervalor.control
		ztec.intervalor.control.generar(ruta_html,ruta_python,cabecera)
	

	def darTipo(valor):
		exec("valor="+valor)
		return valor
	def servir(vista,ruta_html,ruta_python,data={}):
		sys.path.append(ruta_html+"../")
		import settings.roots as roots
		import ztec.zu as zu
		generar(ruta_html+vista+".html",ruta_python+vista+".py","# -*- coding: utf-8 -*-\n")
		f=open(ruta_python+vista+".py","r")
		html=f.read()
		f.close()
		lineas=html.split("\n")
		c=0
		while c<len(lineas):
			if "incluir(" in lineas[c]:
				ini=lineas[c].find("incluir(")+len("incluir(")
				widget=lineas[c][ini:lineas[c].find(")",ini)]
				
				if "," in widget:
					widgets=[]
					w=widget.split(",")
					for elem in w:
						widgets.append(elem[1:-1])
				else:
					widgets=[widget[1:-1]]
				widget=""

				for w in widgets:
					generar(ruta_html+roots.widgets_folder+w+".html",ruta_html+roots.widgets_folder+w+".py","")
					f=open(ruta_html+roots.widgets_folder+w+".py","r")
					widget+=f.read()+"\n"
					f.close()
				

				lineas[c]= zu.tabular(widget,zu.getTab(lineas[c]))

			c+=1
		codigo=""
		for linea in lineas:
			codigo+=linea+"\n"		
		f=open(ruta_python+vista+".py","w")
		f.write(codigo)
		f.close()
		exec(codigo)

	def administrar(rest={}):
		
		modulos={}

		if rest=={}:
			archivo_act=sys.argv[0].split("/")[-1]
			request=cgi.FieldStorage()
			
			orden=request.value
			import ztec.zred as zred
			app="default"
			vista="index"
			





		modulos["servir"]=servir
		if "mod_debug" in rest:
			if rest["mod_debug"]=="False":
				config.mod_debug=False
			elif rest["mod_debug"]=="True":
				config.mod_debug=True

		if config.mod_debug==False:
			if rest=={}:
				appcontroller=config.base_root+config.apps_url+app+"/user/"+config.controller_url
				root_app_current=config.base_root+config.apps_url+app+"/user/"
				url_app_current=config.base_url+config.apps_url+app+"/user/"
				
			else:

				appcontroller=config.base_root+config.apps_url+config.default_app+"/user/"+config.controller_url
				root_app_current=config.base_root+config.apps_url+config.default_app+"/user/"
				url_app_current=config.base_url+config.apps_url+config.default_app+"/user/"
			#print '<meta http-equiv="refresh" content="0;url='+appcontroller+""+ '" /> '
			if rest=={}:
				parametros={'app': app,'vista':vista,"base_root":root_app_current,"base_url":url_app_current}
			else:
				parametros=rest
			
				parametros["base_root"]=root_app_current
				parametros["base_url"]=url_app_current
			
			modulos["ztec"]=ztec
			#Establece coneccion con el controlador de la aplicación
			cnt_file=open(appcontroller,"r")
			cnt=cnt_file.read()
			cnt_file.close()
			exec(cnt)

			cnt(parametros,modulos)
	
		else:

			#appcontroller=config.base_root+config.projects_url+app+"/"+config.controller_url+".py"
			#appcontroller=config.base_root+config.projects_url+app+"/"+config.controller_url+".py"
			
			if "app" not in rest:
				print "Debes pasar la el parametro app con el valor del proyecto para acceder.<br>"
				if "renombrar" in rest:
					if ":" in rest["renombrar"]:
						old,new=rest["renombrar"].split(":")
						os.rename(config.base_root+config.projects_url+old,config.base_root+config.projects_url+new)
					else:
						print "No introdujo los pares viejoNombre:nuevoNombre"
				if "new" in rest:
						shutil.copytree(config.base_root+config.projects_url+config.default_app,config.base_root+config.projects_url+config.default_app+"/../"+rest["new"], symlinks=False, ignore=None)
						print "Ha creado el proyecto: "+rest["new"]
				#rest["new"]
				if "listo" in rest:
					shutil.move(config.base_root+config.projects_url+rest["listo"],config.base_root+config.apps_url)
					print "El proyecto ",rest["listo"]," a pasado a la etapa de producción."
				if "desarrollo" in rest:
					shutil.move(config.base_root+config.apps_url+rest["desarrollo"],config.base_root+config.projects_url)
					print "La aplicación ",rest["desarrollo"]," fue retirada del las aplicaciones en produccion y paso a desarrollo."
				if "ramificar" in rest:
					shutil.copytree(config.base_root+config.apps_url+rest["ramificar"],config.base_root+config.projects_url)
					print "La aplicación ",rest["ramificar"]," paso sea a ramificado."

			else:
				app=rest["app"]
				appcontroller=config.base_root+config.projects_url+app+"/user/"+config.controller_url
				root_app_current=config.base_root+config.projects_url+config.default_app+"/user/"
				url_app_current=config.base_url+config.projects_url+config.default_app+"/user/"	
				parametros=rest
				
				parametros["base_root"]=root_app_current
				parametros["base_url"]=url_app_current
				modulos["ztec"]=ztec
				
				if "renombrar" in rest:
					if ":" in rest["renombrar"]:
						old,new=rest["renombrar"].split(":")
						os.rename(config.base_root+config.projects_url+old,config.base_root+config.projects_url+new)
					else:
						print "No introdujo los pares viejoNombre:nuevoNombre"
				if "new" in rest:
						shutil.copytree(config.base_root+config.projects_url+config.default_app,config.base_root+config.projects_url+config.default_app+"/../"+rest["new"], symlinks=False, ignore=None)
						print "Ha creado el proyecto: "+rest["new"]
				#rest["new"]
				if "listo" in rest:
					shutil.move(config.base_root+config.projects_url+rest["listo"],config.base_root+config.apps_url)
					print "El proyecto ",rest["listo"]," a pasado a la etapa de producción."
				if "desarrollo" in rest:
					shutil.move(config.base_root+config.apps_url+rest["desarrollo"],config.base_root+config.projects_url)
					print "La aplicación ",rest["desarrollo"]," fue retirada del las aplicaciones en produccion y paso a desarrollo."
				if "ramificar" in rest:
					shutil.copytree(config.base_root+config.apps_url+rest["ramificar"],config.base_root+config.projects_url)
					print "La aplicación ",rest["ramificar"]," paso sea a ramificado."
				print appcontroller
				#Establece coneccion con el controlador de la aplicación
				cnt_file=open(appcontroller,"r")
				cnt=cnt_file.read()
				cnt_file.close()
				exec(cnt)

				cnt(parametros,modulos)		

		

except Exception, ex:
	print "<h1>Hay un error: </h1>"
	print "<p>"+str(Exception)[1:-1]+"</p>"
	print "<p>"+str(ex)+"</p>"