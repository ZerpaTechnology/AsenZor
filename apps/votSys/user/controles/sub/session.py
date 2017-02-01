#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
	from modelos.main_model2 import model
	from ztec.zred import setCookie
	import ztec.zu as zu
	import os
	keys=[]
	
	zurl=zred.redirecter(config.base_url,"votSys","index")
	for elem in data:
		keys.append(elem)

	if "getvalue" in dir(data) and  data["action"].value=="sing_up":

		l=[]
		
		l2=["username","email","password","expediente"]
		for elem in l2:
			if elem not in keys:
				print "No llenastes el campo ",elem
				l.append(elem)
			
	
		if l==[]:

			
			#img=p["base_url"]+"../../static/imgs/icono_perfil.jpg"
			#main_model.registrarUsuario(p["nombres"],p["apellidos"],p["correo"],p["password"],img,img)
			
			#zred.sendEmail("zerpatechnolgy@gmail.com",p["correo"],"pendiente","Gracias por registrarte en AsenZor porfavor introduce el siguiente codigo para confirmar tu registro: "+codConfirmacion)
			#---------------------------------------------
			
			codConfirmacion=zu.randomString(4,noalp=False)
			
		
		
			modelo=model(p["base_root"]+"../admin/"+settings.config.model_folder+settings.config.dbs[0],p["base_root"]+"../admin/"+settings.config.resquest_folder,data["username"].value)
			
			token=modelo.registrarUsuario(data["username"].value,data["email"].value,data["password"].value,data["expediente"].value,[p["user_ip"]])
			if token!=False:
				print "logueado"
				zurl("index")
			#zred.clienteSock("localhost",9999,'python zred.sendEmail(jesus26abraham1996@gmail.com,'+p["correo"]+',password,<p>Gracias por registrarte en AsenZor por favor introduce el siguiente código para confirmar tu registro: '+codConfirmacion+'</p> , Asenzor - Codigo de confirmacion)')
			#zred.clienteSock("localhost",9999,'')

			#---------------------------------------------

			if "log" in p and p["log"]=="show":
				print "Se ha enviado un mensaje de confirmación al correo ",p["correo"],"<br>"
				for elem in modelo.db.log:
					print elem.replace("\n","<br>").replace("\x1b[1;31m","<span class='blue'>").replace("\x1b[0m","</span>")
				

				if settings.config.consola==True:
					try:
						for elem in modelo.db.log:
							clienteSock(settings.config.host,settings.config.consola_port,elem,"")
					except Exception as e:
						print e
			
			
		else:
			print "No llenastes los campos: ",l
	if "getvalue" in dir(data) and  data["action"].value=="confirmarUser":
					pass

	if "value" not in dir(data) and data["action"]=="closeSession":
		modelo=model(p["base_root"]+"../admin/"+settings.config.model_folder+settings.config.dbs[0],p["base_root"]+"../admin/"+settings.config.resquest_folder,data["token"])
		respuesta=modelo.closeSession(p["token"],os.environ["REMOTE_ADDR"])

		if respuesta==True:
			print "Ha cerrado session"
			zurl("index")

		

	


	if "getvalue" in dir(data) and data["action"].value=="sing_in":
		
		if "user" in keys and "password" in keys:

			modelo=model(p["base_root"]+"../admin/"+settings.config.model_folder+settings.config.dbs[0],p["base_root"]+"../admin/"+settings.config.resquest_folder,data["user"].value,debug=False)
	
			token=modelo.login(data["user"].value,data["password"].value,os.environ["REMOTE_ADDR"])
		
			if token==True:
				zurl("index")
			
			elif token=="Login":
				zurl("index")
			else:
				zred.charset()
				print "datos invalidos<br>"
				zurl("login")
		else:
			print "datos invalidos"
except Exception, e:
	if config.mod_debug==False:
		print "error en session<br>"
		print e