#!/usr/bin/python
# -*- coding: utf-8 -*-
#============================================================
#Cabecera del controlador
import sys
import time




try:
	def cnt(p,m):

		sys.path.append(p["base_root"]+"../admin/")
		import settings.roots as roots
		import settings.config
		settings.config.p=p
		sys.path.append(p["base_root"]+"../admin/"+roots.libs_folder)
		sys.path.append(p["base_root"]+"../admin/"+roots.models_folder)
		from modelos.main_model2 import model
		import ztec.zu as zu
		import ztec.zred as zred 
		from ztec.zred import zform
		from ztec.zred import clienteSock
		for elem in settings.config.libs_python:
			exec("import "+elem)

		p["AsenZor:Detalles"]={"Versión":0.1,"Autor original":"Jesús Abraham Zerpa Maldonado",
							   "Email":"jesus26abraham1996@gmail.com","Website":"https://zerpatechnology.com.ve",
							   "Actualizaciones":"AsenZor esta en su versión mas reciente"}
		p["AsenZor:chat-box"]={"comentarios":1}
		data=p

		cookie=""
		if "HTTP_COOKIE" in os.environ:
			cookie=os.environ["HTTP_COOKIE"]

		ip=""
		if "REMOTE_ADDR" in os.environ:
			ip=os.environ["REMOTE_ADDR"]
		cookies=cookie.split(" ")
		token=""
		for elem in cookies:
			if "token=" in elem:
				token=elem.replace("token=","")


		if token!="":
			modelo=model(p["base_root"]+"../admin/"+settings.config.model_folder+settings.config.dbs[0],p["base_root"]+"../admin/"+settings.config.resquest_folder,token,debug=False)
			data["token"]=token
			logueado=modelo.consultarLogin(token,os.environ["REMOTE_ADDR"])
		else:
			logueado=False
			data["token"]=""

		data["logueado"]=logueado

		#============================================================
		#Cuerpo del controlador
		#------------------------------------------------------------
		#Sección de parametrisaje

		
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
		if "vista" in p:
			#------------------------------------------------
			#Particiones (sub)
			#carga la vista
			
			for elem in ["vistas"]:
					sub=open(p["base_root"]+roots.controles_folder+roots.sub_folder+elem+".py","r")
					script=sub.read()
					sub.close()
					exec(script)
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
	def action(data,p):

		sys.path.append(p["base_root"]+"../admin/")


		import settings.roots as roots
		import settings.config
		settings.config.p=p
		import os
		sys.path.append(p["base_root"]+"../admin/"+roots.libs_folder)
		sys.path.append(p["base_root"]+"../admin/"+roots.models_folder)
		sys.path.append(p["base_root"]+"../../../modulos/")
		sys.path.append(p["base_root"]+"../../../config/")
		import config.config as config
		for elem in settings.config.libs_python:
			exec("import "+elem)
		import ztec.zu as zu
		import ztec.zred as zred 
		from ztec.zred import clienteSock

		cookie=""
		if "HTTP_COOKIE" in os.environ:
			cookie=os.environ["HTTP_COOKIE"]
		ip=""
		if "REMOTE_ADDR" in os.environ:
			ip=os.environ["REMOTE_ADDR"]
		cookies=cookie.split(" ")

		token=""
		for elem in cookies:
			if "token=" in elem:
				token=elem.replace("token=","")


		if token!="":
			from modelos.main_model2 import model
			modelo=model(p["base_root"]+"../admin/"+settings.config.model_folder+settings.config.dbs[0],p["base_root"]+"../admin/"+settings.config.resquest_folder,token,debug=True)
			p["token"]=token
			logueado=modelo.consultarLogin(token,os.environ["REMOTE_ADDR"])
		else:
			logueado=False
			p["token"]=""




		for elem in ["session","documentation","noticas"]:
				sub=open(config.base_root+config.apps_url+p["app"]+"/user/"+config.controles_dir+"/"+roots.sub_folder+elem+".py","r")
				script=sub.read()
				sub.close()
				exec(script)
		import modelos.main_model2 as main_model2

except Exception, e:
	if config.mod_debug==False:
		print "default<br>",e		