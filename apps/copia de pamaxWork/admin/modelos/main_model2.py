#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
from ztec.zmodel import Model
import sys
import config.config as config
try:
	class model(Model):
		"""docstring for model"""
		#===================================================================
		#Cuerpo del modelo
		def registrarUsuario(self,username,password,email,name,lastname,rank,avatar,department_id,position_id,total_hours=0):
			import datetime
			import ztec.zu as zu
			
			x = datetime.datetime.now()
			print "actualizada ",self.update()
			if self.request():
				self.db("users").insertar(username,password,email,name,lastname,"%s"%x,rank,avatar,department_id,position_id,str(zu.DateTime(H=total_hours)))
				self.db.grabar(self.root_db)

		
		def crearLibro(self,nombre,autores,colaboradores=[],referencias=[],editorial=None,fechaP=None,url=None,costo=None):
			self.update()
			if self.request():
				self.db("libros").insertar(nombre,autores,colaboradores,referencias,editorial,fechaP,url,costo)
				self.db.grabar(self.root_db)

		def guardarTema(self,app,libro,tema,text):
			self.update()
			if self.request:
				self.db("documentos").insertar(app,libro,tema,text)
				self.db.grabar(self.root_db)
				
		def login(self,usuario,password):
			
			self.update()
			if self.request():


				if self.db("users").obtenerFilasValores(usuario)!=[]:
					filas=self.db("users").obtenerFilasValores(usuario)
					if filas[1]==password:
						return True
					else:
						print "la contraseña es incorrecta"
						return False

				

		def closeSession(self,token):
			self.update()
			if self.request():
				filas=self.db("usuarios").obtenerFilasValores(token)
				if filas[6]==token:
					self.db("usuarios").modificarCampo(self.db("usuarios").obtenerFilasId(token)[0],"login",False)
					newToken=zu.randomString()
					while newToken in self.db.obtenerColumna("valor","tokens"):
						newToken=zu.randomString()
					self.db("tokens").modificarCampo(self.db("tokens").obtenerFilasId(token)[0],"valor",newToken)
					self.db.grabar(self.root_db)
					return True
				else:
					return False

		def consultarLogin(self,token):
			self.update()
			if self.request():
				return self.db("usuarios").obtenerFilasValores(token)[-1]
		

except Exception, e:
	if config.mod_debug==False:
		print "error en main_model2<br>"
		print e