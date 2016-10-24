#!/usr/bin/python
try:
	#------------------------------------------------
	#HEAD
	def administrar():
		import controlador as cnt
		
		orden=cnt.request.value
		try:
			app=cnt.darTipo(orden[0].value)
			version=cnt.darTipo(orden[1].value)
			control=cnt.darTipo(orden[2].value)
			vista=cnt.darTipo(orden[3].value)
		except:
			app=orden[0].value
			version=orden[1].value
			control=orden[2].value
			vista=orden[3].value
		if version=="produccion":
			appcontroller=cnt.config.base_root+cnt.config.apps_url+app+"/"+cnt.config.controler_url+cnt.config.templates_url+".py"
		elif version=="error":
			pass
		else:

			appcontroller=cnt.config.base_root+cnt.config.projects_url+app+"/"+version+"/"+app+"/"+cnt.config.controller_url+".py"

	
		f=open(appcontroller,"r")
		text=f.read()
		f.close()
		
		exec(text)
		exec("data="+vista+"()")
		cabecera=""
		for elem in data:
			cabecera+=elem+"="+str(data[elem])+"\n" if type(data[elem])!=str else elem+"="+"'"+data[elem]+"'\n"
		
		#--------------------------------------------------

		if control!="default":
			if version == "produccion":
				
				ruta_python=cnt.config.base_root+cnt.config.apps_url+app+"/"+cnt.config.vistas_url+cnt.config.templates_url+vista+".py"
				ruta_html=cnt.config.base_root+cnt.config.apps_url+app+"/"+cnt.config.vistas_url+vista+".html"
				cnt.generar(ruta_html,ruta_python,cabecera)
				f=open(ruta_python,"r")
				html=f.read()
				f.close()
				exec(html)
				
				
			elif version=="error":
					print "error"
			else:
				if vista!="index":	
					
					ruta_python=cnt.config.base_root+cnt.config.apps_url+app+"/"+cnt.config.vistas_url+cnt.config.templates_url+vista+".py"
					ruta_html=cnt.config.base_root+cnt.config.apps_url+app+"/"+cnt.config.vistas_url+vista+".html"
					cnt.generar(ruta_html,ruta_python,cabecera)
					f=open(ruta_python,"r")
					html=f.read()
					f.close()
					exec(html)
				else:
					ruta_html=cnt.config.base_root+cnt.config.apps_url+app+"/"+cnt.config.vistas_url+"index.html"
					f=open(ruta_html,"r")
					html=f.read()
					f.close()
					exec(html)
		else:

			if version=="produccion":
				if vista!="index":
				
					ruta_python=cnt.config.base_root+cnt.config.apps_url+app+"/"+cnt.config.vistas_url+cnt.config.templates_url+vista+".py"
					ruta_html=cnt.config.base_root+cnt.config.apps_url+app+"/"+cnt.config.vistas_url+vista+".html"
					cnt.generar(ruta_python,ruta_html)
					f=open(ruta_python,"r")
					html=f.read()
					f.close()
					exec(html)
			elif version=="error":
					print "error"

			else:
				
				if vista!="index":	
					
					ruta_python=cnt.config.base_root+cnt.config.projects_url+app+"/"+version+"/"+app+"/"+cnt.config.vistas_url+cnt.config.templates_url+vista+".py"		
					ruta_html=cnt.config.base_root+cnt.config.projects_url+app+"/"+version+"/"+app+"/"+cnt.config.vistas_url+vista+".html"		
					cnt.generar(ruta_html,ruta_python,cabecera)
					f=open(ruta_python,"r")
					html=f.read()
					f.close()
					exec(html)
				else:
					ruta_html=cnt.config.base_root+cnt.config.projects_url+app+"/"+version+"/"+app+"/"+cnt.config.vistas_url+"index.html"
					f=open(ruta_html,"r")
					html=f.read()
					f.close()
					exec(html)

except Exception, ex:
	print "<h1>Hay un error: </h1>"
	print "<p>"+str(Exception)+"</p>"
	print "<p>"+str(ex)+"</p>"