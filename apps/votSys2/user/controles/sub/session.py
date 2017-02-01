#!/usr/bin/env python
# -*- coding: utf-8 -*-
if p["action"]=="sing_up":		
	l=[]
	l2=["correo","password","nombres","apellidos"]
	for elem in l2:
		print elem
		if elem not in p:
			print "No llenastes el campo ",elem
			l.append(elem)
		

	if l==[]:
		img=p["base_url"]+"../../static/imgs/icono_perfil.jpg"
		#main_model.registrarUsuario(p["nombres"],p["apellidos"],p["correo"],p["password"],img,img)
		
		#zred.sendEmail("zerpatechnolgy@gmail.com",p["correo"],"pendiente","Gracias por registrarte en AsenZor porfavor introduce el siguiente codigo para confirmar tu registro: "+codConfirmacion)
		#---------------------------------------------
		codConfirmacion=zu.randomString(4,noalp=False)
		
		main_model2.confirmarUsuario(p["nombres"],p["apellidos"],p["correo"],p["password"],codConfirmacion)
		zred.clienteSock("localhost",9999,'python zred.sendEmail(jesus26abraham1996@gmail.com,'+p["correo"]+',password,<p>Gracias por registrarte en AsenZor por favor introduce el siguiente código para confirmar tu registro: '+codConfirmacion+'</p> , Asenzor - Codigo de confirmacion)')
		#zred.clienteSock("localhost",9999,'')

		#---------------------------------------------

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
if p["action"]=="confirmarUser":
				main_model.registrarUsuario(p["cod"])

if p["action"]=="closeSession":
	main_model.closeSession(p["token"])
	print "Ha cerrado session"
	
if p["action"]=="consultarLogin":
				print main_model.consultarLogin(p["token"])
				print "consulta realizada"
if p["action"]=="sing_in":
	main_model.login(p["user"],p["password"])
	print "te logueas"