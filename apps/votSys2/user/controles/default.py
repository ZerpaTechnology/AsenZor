#!/usr/bin/python
# -*- coding: utf-8 -*-
def cnt(p,m):
	#============================================================
	#Cabecera del controlador
	sys.path.append(p["base_root"]+"../admin/")
	import settings.roots as roots
	import settings.config
	settings.config.p=p
	sys.path.append(p["base_root"]+"../admin/"+roots.libs_folder)
	sys.path.append(p["base_root"]+"../admin/"+roots.models_folder)
	import modelos.main_model as main_model
	import ztec.zu as zu
	import ztec.zred as zred 
	from ztec.zred import clienteSock
	import time
	for elem in settings.config.libs_python:
		exec("import "+elem)

	p["AsenZor:Detalles"]={"Versión":0.1,"Autor original":"Jesús Abraham Zerpa Maldonado",
						   "Email":"jesus26abraham1996@gmail.com","Website":"https://zerpatechnology.com.ve",
						   "Actualizaciones":"AsenZor esta en su versión mas reciente"}
	p["AsenZor:chat-box"]={"comentarios":1}

	#============================================================
	#Cuerpo del controlador
	#------------------------------------------------------------
	#Sección de parametrisaje

	print p
	if "embeber" in p:
		if p["embeber"]=="php":
	 			if "script" in p:
					if os.path.exists(p["base_root"]+"../admin/"+roots.libs_folder+p["script"]):
						functions.ajax(p["base_root"]+"../admin/"+roots.models_folder+roots.ajax_file,{})
						functions.phpload(p["base_url"]+"../admin/"+roots.libs_folder,p["script"],True)
					else:
						print "El script no existe"
				else:
					print "Debes pasar el parametro 'script' con el nombre del script de php a cargar"
		
	if "action" in p:
			#------------------------------------------------------------
			#Particiones (sub)
			for elem in ["session","documentation"]:
				sub=open(p["base_root"]+roots.controles_folder+roots.sub_folder+elem+".py","r")
				script=sub.read()
				sub.close()
				exec(script)

			print "<div class='width-100p height-auto bg-ubuntu_jet white pad-t05 pad-b05 text-center'>"

			print "</div>"
	
	if "form" in p:

		print '<META HTTP-EQUIV="REFRESH" CONTENT="0;URL=' +config.base_url+'">'
	if "vista" in p:
		#carga la vista
		data=p
		try:
			if "admin" in p and zred.normalizar(p["admin"])==True:
				m["servir"](p["vista"],p["base_root"]+"../admin/"+roots.vistas_folder,p["base_root"]+"../admin/"+roots.templates_url,data=data)
			else:
				m["servir"](p["vista"],p["base_root"]+roots.vistas_folder,p["base_root"]+roots.templates_url,data=data)
		except Exception as e:
			print "Ha occurido un error en el motor de plantillas<br>"
			print e

			
		
	

	#--------------------------------------------------------------
	#Sección de testeo
	#main_model.registrarUsuario("jesus","zerpa","jesus26abraham1996@gmail.com",1234,p["base_root"]+"AsenZor/static/imgs/icono_perfil.jpg",[])
	
	#print fecha
	#print "<br>"
