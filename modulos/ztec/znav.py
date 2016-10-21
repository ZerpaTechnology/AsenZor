#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
#10-1-2015
import os, sys, glob, platform

def conv_l_c(lista,cadena=""): #convertir lista a cadena
	c=""
	for elem in lista:
		c=c+str(elem)+cadena
	return c

def compar(valor1,valor2): #comparar dos valores 
	comparador=0
	for elem in valor1:
		for elem2 in valor2:
			if elem==elem2:
				comparador+=1
			if comparador==len(valor1)-1:
				return True
			else:
				return False	



def retro(valor):#retroceder

	sistema=platform.system()
	if sistema == "Linux":
		directorio=valor.split("/")
	if sistema == "Window":
		directorio=valor.split("//")
	if sistema == "Darwin":
		directorio=valor.split(":")
	return directorio

class znav:
	def __init__(self):
		self.ruta=os.getcwd()
		sistema=platform.system()
		if sistema=="Linux":
			self.separador="/"
		if sistema=="Window":
			self.separador="//"
		if sistema=="Darwin":
			self.separador=":"		
	def nav(self,nombre=""):#navegar
		self.todos=glob.glob(self.ruta+"/*")
		if nombre != "" and type(nombre) != int:
			try:
			    for elem in self.todos:
				    if elem.count(self.separador+nombre)==1:
				
					self.ruta=elem

					
			except:
				print "ese directorio no existe"
		if nombre=="" or type(nombre) == int:
			if type(nombre)==int:
				n=nombre
			else:
				n=1
			retroceso=retroceder(self.ruta)
			c=0
			while c < n: 
				retroceso.remove(retroceso[len(retroceso)-1])
				c+=1
			self.ruta=conv_l_c(retroceso,self.separador)
		
	def sel(self,archivo):#seleccionar
		self.todos=glob.glob(self.ruta+"/*")
		for elem in self.todos:
					if elem.count(archivo)==1:
						if archivo.count(self.separador)==0:
							r=self.ruta+self.separador+archivo
							return r
					else:
						print "no has seleccionado un archivo o no le has colocado extención"

					
	def ver(self):#ver
		return glob.glob(self.ruta+"/*")

	def act(self):#ruta actual
		return self.ruta

	def imp(self):#importar modulo
		sys.path.append(self.ruta)
		
	def vers(self):#version
		print "NavegadorPath v0.1"
		
	
