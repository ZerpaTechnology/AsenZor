#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
import sys
import os
import time
from zdb import DB

class Model:
	"""docstring for Model"""
	def __init__(self,dbfile,resquest_folder,token,debug=False):
		try:

			self.dbfile=dbfile
			self.resquest_folder=resquest_folder
			self.token=token
			self.root_db=self.dbfile+"_db.py"
	
			#Cabecera del modelo

			#sys.path.append("../config")
			
			import zu
			
			
			tiempo=time.time()
		
			if os.path.exists(self.dbfile+"_db.py"):
				self.db=DB(self.dbfile+"_db.py",debug=debug)

	
			else:
				f=open(self.dbfile+"_struct.py","r")
				struct=f.read()
				f.close()
				exec(struct)
				
				self.db=db


			
			self.db.debug=debug

		except Exception, e:
			if self.db.debug==True:
				print "error en zmodel"
				print e

	def update(self):

		if os.path.exists(self.dbfile+"_db.py"):
			self.db=DB(self.dbfile+"_db.py")
			return True
		else:
			return False



	def request(self):

		#espera a tener un listado de archivos
		time.sleep(0.1)
		#se mantiene en espera si se esta utilizando la base de datos
		
		while "ordenDB.py" in os.listdir(self.resquest_folder):
			pass
	
		#lee los archivos listado en la base de datos

		elementos=os.listdir(self.resquest_folder)
		f=open(self.resquest_folder+self.token+"Request.py","w")
		f.write("")
		f.close()

		f=open(self.resquest_folder+"ordenDB.py","w")
		if elementos!=[]:
			f.write("orden="+str(elementos))
		else:
			f.write("orden="+str([self.token+"Request.py"]))
		f.close()
		#Espera que se defina el archivo de orden

		time.sleep(0.1)

		f=open(self.resquest_folder+"ordenDB.py","r")
		txt=f.read()
		f.close()
		exec(txt)
		c=0
		
		while len(orden)>0:
	
			if orden[c]==self.token+"Request.py":
				
				del orden[c]
				f=open(self.resquest_folder+"ordenDB.py","w")
				f.write("orden="+str(orden))
				f.close()
				os.remove(self.resquest_folder+self.token+"Request.py")
				if orden==[]:
					os.remove(self.resquest_folder+"ordenDB.py")
				return True
			
			c+=1

		




		


		
		