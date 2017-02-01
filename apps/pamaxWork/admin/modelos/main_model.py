#!/usr/bin/env python
# -*- coding: utf-8 -*-
#====================================================================

#Cabecera del modelo
import sys
import os
#sys.path.append("../config")
import random
import settings.roots as roots
import settings.config 
from ztec.zdb import DB
from ztec import zu
from ztec import zred
name_db=settings.config.dbs[0] #main_db
p=settings.config.p
root_db=p["base_root"]+"../admin/"+roots.models_folder+name_db+"_db.py"
import time
tiempo=time.time()
if os.path.exists(p["base_root"]+"../admin/"+roots.models_folder+name_db+"_db.py"):
	db=DB(p["base_root"]+"../admin/"+roots.models_folder+name_db+"_db.py")
else:
	f=open(p["base_root"]+"../admin/"+roots.models_folder+name_db+"_struct.py","r")
	struct=f.read()
	f.close()
	exec(struct)
#===================================================================
#Cuerpo del modelo
def confirmarUsuario(nombres,apellidos,correo,password,codigo,db=db):
	
	db("confirmacion").insertar(nombres,apellidos,correo,password,codigo)
	db.grabar(root_db)

def registrarUsuario(cod,foto=None,imgs=None,db=db):
	filas=db("confirmacion").obtenerFilasValores(cod)
	print filas
	for elem in db("confirmacion").obtenerFilasId(cod):
		db("confirmacion").delFila(elem)
	token=zu.randomString()
	while token in db.obtenerColumna("valor","tokens"):
		token=zu.randomString()

	if cod==filas[4]:
		db("usuarios").insertar(filas[0],filas[1],filas[2],filas[3],foto,imgs,token)
		db("tokens").insertar(filas[2],token,str(zu.DateTime()),str(zu.DateTime(w=4)))
		i=len(db.obtenerColumna("token","usuarios"))-1
		db("tokens").relacionar(i,"usuario",tabla="usuarios",campo="correo",id=i)
		db("usuarios").relacionar(i,"token",tabla="tokens",campo="valor",id=i)
		db.grabar(root_db)
	else:
		print filas," - ",cod
		print "el codigo de confirmacion no coincide"

def crearLibro(nombre,autores,colaboradores=[],referencias=[],editorial=None,fechaP=None,url=None,costo=None,db=db):

	db("libros").insertar(nombre,autores,colaboradores,referencias,editorial,fechaP,url,costo)
	db.grabar(root_db)

def guardarTema(app,libro,tema,text,db=db):
	db("documentos").insertar(app,libro,tema,text)
	db.grabar(root_db)
	
def login(usuario,password,db=db):
	if db("usuarios").obtenerFilasValores(usuario)[-1]==False:
		filas=db("usuarios").obtenerFilasValores(usuario)

		if filas[3]==password:

			db("usuarios").modificarCampo(db("usuarios").obtenerFilasId(usuario)[0],"login",True)
			
			db.grabar(root_db)
			return True
		else:
			print "la contraseña es incorrecta<br>"
			return False
	else:
		print "Este usuario ya esta logueado<br>"
		return True
	

def closeSession(token,db=db):
	filas=db("usuarios").obtenerFilasValores(token)
	
	if filas[6]==token:
		db("usuarios").modificarCampo(db("usuarios").obtenerFilasId(token)[0],"login",False)

		newToken=zu.randomString()
		
		while newToken in db.obtenerColumna("valor","tokens"):
			newToken=zu.randomString()
		db("tokens").modificarCampo(db("tokens").obtenerFilasId(token)[0],"valor",newToken)
		db.grabar(root_db)
		return True
	else:
		return False

def consultarLogin(token,db=db):
	return db("usuarios").obtenerFilasValores(token)[-1]