#!/usr/bin/python
try:
	#------------------------------------------------
	#HEAD
	def administrar():
		import controlador as cnt
		
		orden=cnt.request.value
		
		try:
			app=cnt.darTipo(orden[0].value)
			vista=cnt.darTipo(orden[1].value)
		except:
			app=orden[0].value

			vista=orden[1].value

		print vista
		print app
		print "<br>"

		if cnt.config.mod_debug==False:
			appcontroller=cnt.config.base_url+cnt.config.apps_url+app+"/"+cnt.config.controller_url
			print appcontroller
			print '<meta http-equiv="refresh" content="0;url='+appcontroller+ '" /> '
			print "3"

		elif cnt.config==True:
			pass
		else:

			#appcontroller=cnt.config.base_root+cnt.config.projects_url+app+"/"+cnt.config.controller_url+".py"
			pass
			appcontroller=cnt.config.base_root+cnt.config.projects_url+app+"/"+cnt.config.controller_url+".py"
			print "5"
			
			print "<br>"
		

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
		if cnt.config.mod_debug==False:
			pass
			"""
			ruta_python=cnt.config.base_root+cnt.config.apps_url+app+"/"+cnt.config.vistas_url+cnt.config.templates_url+vista+".py"
			ruta_html=cnt.config.base_root+cnt.config.apps_url+app+"/"+cnt.config.vistas_url+vista+".html"
			cnt.generar(ruta_html,ruta_python,cabecera)
			f=open(ruta_python,"r")
			html=f.read()
			f.close()
			exec(html)
			"""
			

			"""
			if vista!="index":	
				
				ruta_python=cnt.config.base_root+cnt.config.projects_url+app+"/"+cnt.config.vistas_url+cnt.config.templates_url+vista+".py"
				ruta_html=cnt.config.base_root+cnt.config.projects_url+app+"/"+cnt.config.vistas_url+vista+".html"
				cnt.generar(ruta_html,ruta_python,cabecera)
				f=open(ruta_python,"r")
				html=f.read()
				f.close()
				exec(html)
			else:
				ruta_html=cnt.config.base_root+cnt.config.projects_url+app+"/"+cnt.config.vistas_url+"index.html"
				f=open(ruta_html,"r")
				html=f.read()
				f.close()
				print html
			"""



except Exception, ex:
	print "<h1>Hay un error: </h1>"
	print "<p>"+str(Exception)+"</p>"
	print "<p>"+str(ex)+"</p>"