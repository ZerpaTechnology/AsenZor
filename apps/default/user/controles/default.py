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
	from ztec.zred import clienteSock
	import time


	for elem in settings.config.libs_python:
		exec("import "+elem)
	#============================================================
	#Cuerpo del controlador
	#------------------------------------------------------------
	#Sección de parametrisaje
	

		
	if "action" in p:
		if p["action"]=="phpload":
			if "script" in p:
				if os.path.exists(p["base_root"]+"../admin/"+roots.libs_folder+p["script"]):
					functions.ajax(p["base_root"]+"../admin/"+roots.models_folder+roots.ajax_file,{})
					functions.phpload(p["base_url"]+"../admin/"+roots.libs_folder,p["script"],True)
				else:
					print "El script no existe"
			else:
				print "Debes pasar el parametro 'script' con el nombre del script de php a cargar"
		else:
			print "<div class='width-100p height-auto bg-ubuntu_jet white pad-t05 pad-b05 text-center'>"
			if p["action"]=="sing_up":
				l=["correo","password","nombres","apellidos"]
				for elem in l:
					if elem not in p:
						print "No llenastes el campo ",elem
				if l==[]:
					img=p["base_url"]+"../../static/imgs/icono_perfil.jpg"
					main_model.registrarUsuario(p["nombres"],p["apellidos"],p["correo"],p["password"],img,img)
					if "log" in p and p["log"]=="show":
						print "Se ha enviado un mensaje de confirmación al correo ",p["correo"],"<br>"
						for elem in main_model.db.log:
							print elem.replace("\n","<br>").replace("\x1b[1;31m","<span class='blue'>").replace("\x1b[0m","</span>")
						

						if settings.config.consola==True:
							try:
								for elem in main_model.db.log:
									clienteSock(settings.config.host,settings.config.consola_port,elem,"")
							except Exception as e:
								print e
					
					
				else:
					print "No llenastes los campos: ",l

			if p["action"]=="crearLibro":
					main_model.crearLibro("defaysult",["Jesús Zerpa"])

			if p["action"]=="guardarTema":
					main_model.guardarTema()

			print "</div>"
	if "vista" in p:
		#carga la vista
		data=p
		m["servir"](p["vista"],p["base_root"]+roots.vistas_folder,p["base_root"]+roots.templates_url,data=data)
	

	#--------------------------------------------------------------
	#Sección de testeo
	#main_model.registrarUsuario("jesus","zerpa","jesus26abraham1996@gmail.com",1234,p["base_root"]+"AsenZor/static/imgs/icono_perfil.jpg",[])
	
	#print fecha
	#print "<br>"
