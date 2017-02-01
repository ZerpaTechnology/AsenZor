#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:

	from modelos.main_model2 import model
	keys=[]
	for elem in data:
		keys.append(elem)

	if data["action"].value=="sing_up":

		l=[]
		l2=["email","password","name","lastname","rank","avatar","department_id","position_id"]
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

		
		
			modelo=model(p["base_root"]+"../admin/"+settings.config.model_folder+settings.config.dbs[0],p["base_root"]+"../admin/"+settings.config.resquest_folder,data["user"].value,debug=True)
			
			modelo.registrarUsuario(data["user"].value,data["password"].value,data["email"].value,data["name"].value,data["lastname"].value,int(data["rank"].value),data["avatar"].value,int(data["department_id"].value),int(data["position_id"].value))
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
	if data["action"].value=="confirmarUser":
					main_model.registrarUsuario(p["cod"])

	if data["action"].value=="closeSession":
		main_model.closeSession(p["token"])
		print "Ha cerrado session"
		
	if data["action"].value=="consultarLogin":
					print main_model.consultarLogin(p["token"])
					print "consulta realizada"
	if data["action"].value=="sing_in":
		if "user" in keys and "password" in keys:
			modelo=model(p["base_root"]+"../admin/"+settings.config.model_folder+settings.config.dbs[0],p["base_root"]+"../admin/"+settings.config.resquest_folder,data["user"].value,)
			if modelo.login(data["user"].value,data["password"].value):
				print zred.redirect(p["base_url"]+"app="+p["app"]+"&vista=index2")
			else:
				zred.charset()
				print "datos invalidos<br>"
		else:
			print "datos invalidos"
except Exception, e:
	if config.mod_debug==False:
		print "error en session<br>"
		print e