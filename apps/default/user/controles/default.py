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
	import time


	for elem in settings.config.libs_python:
		exec("import "+elem)
	#============================================================
	#Cuerpo del controlador
	#------------------------------------------------------------
	#Sección de parametrisaje
	
	if settings.config.consola==True:
		import socket
		msj =""
		host, port = "localhost" , 9999
		#creo un socket y me conecto
		sock= socket.socket()
		sock.connect((host,port))
		enviar=True
		print "Ingrese un mensaje o salir para terminar"
		while msj != "salir":
		    msj = "hola mundo"
		    #intento mandar msj
		    try:
		        sock.send(msj)
		        msj="salir"
		    # si no se puede entonces salgo
		    except:
		        print "no se mando el mensaje"
		        msj="salir"
		    
		sock.close() #recuerden cerrar el socket
		
		
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
				l=[]
				if "correo" not in p:
					l.append("correo")
				if "password" not in p:
					l.append("password")
				if "nombres" not in p:
					l.append("nombres")
				if "apellidos" not in p:
					l.append("apellidos")
				if l==[]:
					img=p["base_url"]+"../../static/imgs/icono_perfil.jpg"
					main_model.registrarUsuario(p["nombres"],p["apellidos"],p["correo"],p["password"],img,img)
					print "Se ha enviado un mensaje de confirmación al correo ",p["correo"]

				else:
					print "No llenastes los campos: ",l

			print "</div>"
	if "vista" in p:
		#carga la vista
		m["servir"](p["vista"],p["base_root"]+roots.vistas_folder,p["base_root"]+roots.templates_url)
	
	
	#--------------------------------------------------------------
	#Sección de testeo
	#main_model.registrarUsuario("jesus","zerpa","jesus26abraham1996@gmail.com",1234,p["base_root"]+"AsenZor/static/imgs/icono_perfil.jpg",[])
	
	#print fecha
	#print "<br>"
