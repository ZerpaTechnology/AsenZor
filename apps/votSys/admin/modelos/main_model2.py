#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
from ztec.zmodel import Model
from  ztec.zred import  setCookie
import sys
import ztec.zu as zu
try:
	import config.config as config
except:
	import config
try:
	class model(Model):
		"""docstring for model"""
		#===================================================================
		#Cuerpo del modelo
		def registrarUsuario(self,username,email,password,expediente,ips):
			import datetime
			
			
			
			x = datetime.datetime.now()
			self.update()
			if self.request():
				token=zu.randomString()
				while token in self.db("users").obtenerColumna("token"):
					token=zu.randomString()

				#Al parecer el motor de bases de datos esta funcionando perfecto con la insercion y relaciones
				self.db('users').insertar(username, 'mailto:'+email, 'password:'+password, token,int(expediente),ips, True)
				self.db('tokens').insertar(username, token, 'datetime:'+zu.DateTime(ignorar=[":%S"]), 'datetime:'+zu.DateTime(H=4,ignorar=[":%S"]))
				
				i=self.db("users").obtenerFilasId(username)[0]

				self.db('users').relacionar(i,'token',campo= 'value',tabla= 'tokens',id= i,)
				self.db("users").relacionar(i,"username",id=i,tabla="tokens",campo="user")
				
				self.db.grabar(self.root_db)
				setCookie("token="+token)

				return token

		
		def crearNoticia(self,titulo,img,noticia):
			self.update()
			if self.request():
				self.db("noticias").insertar(titulo,img,noticia)
				self.db.grabar(self.root_db)

		def guardarTema(self,app,libro,tema,text):
			self.update()
			if self.request:
				self.db("documentos").insertar(app,libro,tema,text)
				self.db.grabar(self.root_db)
				
		def login(self,usuario,password,ip):
			import ztec.zu as zu
			self.update()
			if self.request():

				
				if self.db("users").obtenerFilasValores(usuario)!=[]:
					if  self.db("users").obtenerFilasValores(usuario)[6]==False:
					
						if usuario in self.db("users").obtenerColumna("username"):
							filas=self.db("users").obtenerFilasValores(usuario)

							
							if filas[2]==password:	
								token=zu.randomString()
								while token in 	self.db("users").obtenerColumna("token"):
									token=zu.randomString()

								if ip not in filas[5]:
									filas[5].append(ip)
									
									self.db("users").modificarCampo(self.db("users").obtenerFilasId(usuario)[0],"ip´s",filas[4])

								self.db("tokens").modificarCampo(self.db("tokens").obtenerFilasId(usuario)[0],"value",token)
								self.db("users").modificarCampo(self.db("users").obtenerFilasId(usuario)[0],"login",True)
								
								
								
								setCookie("token="+token)
								self.db.grabar(self.root_db)
								return True
							else:
								return False

					else:
						filas=self.db("users").obtenerFilasValores(usuario)
						
						token=zu.randomString()
						while token in self.db("users").obtenerColumna("token"):
							token=zu.randomString()

						if filas[2]==password:	
							self.db("tokens").modificarCampo(self.db("tokens").obtenerFilasId(usuario)[0],"value",token)
							self.db("tokens").modificarCampo(self.db("tokens").obtenerFilasId(usuario)[0],"nace",'datetime:'+zu.DateTime(ignorar=[":%S"]))
							self.db("tokens").modificarCampo(self.db("tokens").obtenerFilasId(usuario)[0],"muere",'datetime:'+zu.DateTime(H=4,ignorar=[":%S"]))
							
							if ip not in filas[5]:
									filas[5].append(ip)
									self.db("users").modificarCampo(self.db("users").obtenerFilasId(usuario)[0],"ip´s",filas[4])

							setCookie("token="+token)
							self.db.grabar(self.root_db)

							return "Login"

				else:
					return False

				

		def closeSession(self,token,ip):
			self.update()
			if self.request():
				filas=self.db("users").obtenerFilasValores(token)
				
				if filas[3]==token and ip in self.db("users").obtenerFilasValores(token)[5]:
					self.db("users").modificarCampo(self.db("users").obtenerFilasId(token)[0],"login",False)
					newToken=zu.randomString()
					while newToken in self.db.obtenerColumna("value","tokens"):
						newToken=zu.randomString()
					self.db("tokens").modificarCampo(self.db("tokens").obtenerFilasId(token)[0],"value",newToken)
					self.db.grabar(self.root_db)
					return True
				else:
					return False

		def consultarLogin(self,token,ip):
			try:	
				from datetime import datetime
				self.update()
				if self.request():


					if self.db.tablas["users"]!= {} and self.db.tablas["users"][0][3].valor==token:
						

						if token== self.db("users").obtenerFilasValores(token)[3] and ip in self.db("users").obtenerFilasValores(token)[5]:
							
							if self.db("users").obtenerFilasValores(token)[6]==True:
								
								formato=self.db.campos["tokens"][2][9]
								
								nace=datetime.strptime(self.db("tokens").obtenerFilasValores(token)[2],formato)
								muere=datetime.strptime(self.db("tokens").obtenerFilasValores(token)[3],formato)
								
								if nace<muere:


									return True
								else:
								
									newToken=zu.randomString()
									
									while newToken in self.db.obtenerColumna("value","tokens"):
										newToken=zu.randomString()

									self.db("tokens").modificarCampo(self.db("tokens").obtenerFilasId(token)[0],"value",newToken)

									return newToken
							else:
								setCookie("")
								return False

						else:
							setCookie("")
							return False
					else:
									
						return False
			except Exception,e:
					print "error en model -> consultarLogin"
					print e

except Exception, e:
	if config.mod_debug==False:
		print "error en main_model2<br>"
		print e