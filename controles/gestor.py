#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
	#------------------------------------------------
	#HEAD
	import cgi
	import os
	import time
	import sys
	import httplib, urllib
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
	def servir(vista,ruta_html,ruta_python):
		sys.path.append(ruta_html+"../")
		import settings.roots as roots
		import ztec.zu as zu
		generar(ruta_html+vista+".html",ruta_python+vista+".py","")
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
			
			try:
				app=darTipo(orden[0].value)
				vista=darTipo(orden[1].value)
			except:
				app=orden[0].value

				vista=orden[1].value




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
			"""
			def incluir(widget,admin=False,current):
				sys.path.append(root_app_current+"../admin/")
				import settings.roots as roots
				if admin==True:
					servir(root_app_current+"../admin/"+roots.widgets_url+widget+".html",root_app_current+"../admin/"+roots.widgets_url+widget+".html")
				else:
					servir(root_app_current+roots.widgets_url+widget+".html",root_app_current+roots.widgets_url+widget+".html")

			"""
			modulos["ztec"]=ztec
			#Establece coneccion con el controlador de la aplicación
			cnt_file=open(appcontroller,"r")
			cnt=cnt_file.read()
			cnt_file.close()
			exec(cnt)

			cnt(parametros,modulos)
	
		else:

			#appcontroller=config.base_root+config.projects_url+app+"/"+config.controller_url+".py"
			appcontroller=config.base_root+config.projects_url+app+"/"+config.controller_url+".py"
			
			
		
		

		"""
		f=open(appcontroller,"r")
		text=f.read()
		f.close()
		
		exec(text)
		exec("data="+vista+"()")
	
		cabecera=""
		for elem in data:
			cabecera+=elem+"="+str(data[elem])+"\n" if type(data[elem])!=str else elem+"="+"'"+data[elem]+"'\n"
		"""	

		#--------------------------------------------------
		if config.mod_debug==False:
			pass
			
			
			

			"""
			if vista!="index":	
				
				ruta_python=config.base_root+config.projects_url+app+"/"+config.vistas_url+config.templates_url+vista+".py"
				ruta_html=config.base_root+config.projects_url+app+"/"+config.vistas_url+vista+".html"
				generar(ruta_html,ruta_python,cabecera)
				f=open(ruta_python,"r")
				html=f.read()
				f.close()
				exec(html)
			else:
				ruta_html=config.base_root+config.projects_url+app+"/"+config.vistas_url+"index.html"
				f=open(ruta_html,"r")
				html=f.read()
				f.close()
				print html
			"""



except Exception, ex:
	print "<h1>Hay un error: </h1>"
	print "<p>"+str(Exception)+"</p>"
	print "<p>"+str(ex)+"</p>"