#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zdb #zerpa base de datos
import zwx #zerpa interfaz
import zt  #zerpa traductor
import thread
import css
import random
import zu
import copy



try:
	import pygame
	from pygame.locals import *
	v_pygame=True
except:
	v_pygame=False

def tipo(valor):
	tipos={"<type 'int'>":'int',"<type 'bool'>":'bool',"<type 'str'>":'str'}
	if valor in tipos:
		return tipos[valor]		
	else:
		if type(valor)==str:
			valor="'"+valor+"'"
			return valor
		else:
			return valor
		
def memoria1(bit,l,valor):
	if len(l) < bit:
		l.append(valor)
	else:
		l.remove(l[0])
		l.append(valor)
	return l
	
		
class Zmadre:
	def __init__(self,nombre,manual,pantalla=None,idioma="es",herencia=None):
		#---------------------------------------------------------------
		#ATRIBUTOS ESPECIALES
		self.salida=None
		self.entrada={}
		self.funciones={}
		self.nombre=nombre	
		self.tipo=None
		self.documentacion={nombre:manual}
		self.idioma=idioma
		self.zt=zt.ZT(self.idioma)
		self.herencia=herencia
		self.css=css.CSS(pantalla)
		self.objetos={"funciones":{},"atributos":{}}
		self.funciones={}
					
	def atributo(self,nombre,valor=None,dimension=[]):
		#print 'self.objetos["atributos"]['+str(nombre)+']'+zu.dimensionar(dimension)+'='+str(valor),"esto es atributo"
		exec('self.objetos["atributos"][nombre]'+zu.dimensionar(dimension)+'=valor')
		self.salida=["atributo",nombre,valor]

		
	def actualizar_atributos(self):
		self.salida=["actualizar_atributos",self.atributos]
		
	def recibir(self,bit,*entrada):
		for elem in entrada:
			if elem[0] in self.entrada:
				self.entrada[elem[0]]=memoria1(bit,self.entrada[elem[0]],elem[1])
			else:
				self.entrada[elem[0]]=[elem[1]]
			
	def cfuncion(self,nombre,argumentos,documentacion,codigo,sobrescribir=False):

			if nombre not in self.objetos["funciones"]:
				if type(argumentos)==list or type(argumentos)==tuple:		
					parametros=""
					puede=True
					if int in argumentos:
							puede=False
					if bool in argumentos:
							puede=False
					if dict in argumentos:
							puede=False
					if tuple in argumentos:
							puede=False
					if list in argumentos:
							puede=False
											
					if puede == True:
						for elem in argumentos:
							parametros=parametros+elem+","
						codigo="def "+nombre+"("+parametros[:-1]+"):\n "+codigo
						self.objetos["funciones"][nombre]=codigo
						self.cargar_funciones()
						
						
						
				elif type(argumentos)==str:
					
					codigo="def "+nombre+"("+argumentos+"):\n "+codigo
					self.objetos["funciones"][nombre]=codigo
					self.cargar_funciones()
					
				elif type(argumentos)==dict:
					parametros=""	
					for elem in argumentos["OR"]:
						if argumentos[elem] != "":
							parametros=parametros+elem+"="+str(argumentos[elem])+","
						else:
							parametros=parametros+elem+","
					codigo="def "+nombre+"("+parametros[:-1]+"):\n "+codigo
					self.objetos["funciones"][nombre]=codigo	
					self.cargar_funciones()				
						
				else:
					print "los datos pasados por argumentos no son validos"
					print "los datos deven ser:"
					print "    una lista con cadenas dentro"
					print "    una cadena"
					print "    una un diccionario con cadenas como clave"		
			else:
				print "esa funcion ya existe o hay un objeto con ese mismo nombre"
				print "si deseas sobrescribirla agrega (True) como parametro final"				

	def cargar_funciones(self):
		for elem in self.objetos["funciones"]:
			exec(self.objetos["funciones"][elem])
			exec("self.funciones['"+elem+"']="+elem)

		
			
	def enviar(self):
		return [self.nombre,self.salida]	
		
	def ayuda(self,buscar):
		if buscar in self.documentacion:
			print self.zt.t(self.documentacion[buscar])
			return self.zt.t(self.documentacion[buscar])
		else:
			print "el valor a buscar no existe, introdusca algunos de estos:"
			for elem in self.documentacion.keys():
				print elem
				
	def doc(self,nombre,manual,puerta=False):
		if puerta==False:
			if nombre in self.documentacion==False:
				self.documentacion[nombre]=manual
			else:
				print "ya este campo existe si desea remplazarlo agregue (False) al final de la función"
		else:
			self.documentacion[nombre]=manual

class Z:
	def __init__(self,app,pantalla=None,idioma="es"):
		self.app=app
		self.idioma=idioma
		self.css=css.CSS(pantalla)
		self.objetos={"app":{},
					  "pantalla":{"x":[],"y":[]},
					  "funciones":{},#libreria de funciones
					  }
		self.funciones={}
		self.conexiones={}
		self.entrada=""

		
	def obj(self,nombre,doc,hereda=None):
		self.objetos["app"][nombre]=Zmadre(nombre,doc,self.idioma,hereda)
		
	def conectar(self,obj1,obj2,bit=5):
		self.conexiones[obj1]=[obj2,bit]
	def fusionar(self,app,sobrescribir=False):
		if app.app not in self.objetos["app"]:
			self.objetos["app"][app.app]=app
			self.objetos["app"][app.app].cargar_funciones()
		else:
			if sobrescribir==True:
				self.objetos["app"][app.app]=app
			else:
				print "esta aplicación ya se encuentra en esta aplicación"
				print "si desea sobrescribirla agrege (True) como parametro final"

	def cfuncion(self,nombre,argumentos,documentacion,codigo,sobrescribir=False):

		if nombre not in self.objetos["funciones"]:
			if type(argumentos)==list or type(argumentos)==tuple:		
				parametros=""
				puede=True
				if int in argumentos:
						puede=False
				if bool in argumentos:
						puede=False
				if dict in argumentos:
						puede=False
				if tuple in argumentos:
						puede=False
				if list in argumentos:
						puede=False
										
				if puede == True:
					for elem in argumentos:
						parametros=parametros+elem+","
					codigo="def "+nombre+"("+parametros[:-1]+"):\n "+codigo
					self.objetos["funciones"][nombre]=codigo
					self.cargar_funciones()
					
					
					
			elif type(argumentos)==str:
				codigo="def "+nombre+"("+argumentos+"):\n "+codigo
				self.objetos["funciones"][nombre]=codigo
				self.cargar_funciones()
				
			elif type(argumentos)==dict:
				parametros=""	
				for elem in argumentos["OR"]:
					if argumentos[elem] != "":
						parametros=parametros+elem+"="+str(argumentos[elem])+","
					else:
						parametros=parametros+elem+","
				codigo="def "+nombre+"("+parametros[:-1]+"):\n "+codigo
				self.objetos["funciones"][nombre]=codigo	
				self.cargar_funciones()				
					
			else:
				print "los datos pasados por argumentos no son validos"
				print "los datos deven ser:"
				print "    una lista con cadenas dentro"
				print "    una cadena"
				print "    una un diccionario con cadenas como clave"		
		else:
			print "esa funcion ya existe o hay un objeto con ese mismo nombre"
			print "si deseas sobrescribirla agrega (True) como parametro final"				

	def cargar_funciones(self):
		for elem in self.objetos["funciones"]:
			exec(self.objetos["funciones"][elem])#crea la funcion en el distema "def f(): codigo"
			exec("self.funciones['"+elem+"']="+elem)
			
			
			
								
	def correr_conexiones(self):
		if self.conexiones !={}:
			for elem in self.conexiones:
					self.objetos[elem].recibir(self.conexiones[elem][1],self.objetos[self.conexiones[elem][0]].enviar())
		
	#-----------------------------------------------------------------------	

	#-----------------------------------------------------------------------		
			
"""
	
objeto=Z()
objeto.obj("obj1","objeto de prueba1")
objeto.obj("obj2","objeto de prueba2")
objeto.objetos["obj2"].atributo("edad","12")
objeto.conectar("obj1","obj2")
#--------
objeto.correr_conexiones()
#--------
print objeto.objetos["obj1"].entrada
			
			
"""
