#!/usr/bin/env python
# -*- coding: utf-8 -*-

email="<type 'email'>"
#Estado:
#version:v0.01
"""
la función DB permite crear base de datos de manera sencilla 
"""
class obj:
	def __init__(self,valor):
		self.valor=valor
		
def DB(dbfile=None,debug=False):
        def db(tabla):
			    self=db
					
				
				#nuevo uso del registro, almacena todos los comandos utilizados
				#para que estos luego puedan ser escritos en un archivo aparte
			    if tabla not in self.tablas and tabla not in self.campos:
					self.campos[tabla]=[]
					self.tablas[tabla]={}
					self.clavePrimaria[tabla]=0
			    self.seleccion=tabla
			    self.idseleccion=None
			    
					

				
			    #Estado:finalizado 
			    #version:v0.01
			    """dbtype permite identificar un tipo de dato que pertenece a los tipos de datos que trabaja la base de datos"""
			    def dbtype(dato):

					if type(dato)==str:
						if "@" in dato and ".com" in dato[dato.index("@"):]:
							return "<type 'email'>"
						elif "/" in dato and "/" in dato[dato.index("/"):] and "/" in dato[len(dato[dato.index("/"):]):]:
							t=dato.split(" ")
							if ":" in t[1] and "m" in t[1][t[1].index(":"):]:
								return "<type 'datetime'>"
							else:
								t=dato.split("/")
								if len(t[0])==2 and len(t[1])==2:
									return "<type 'date'>"
						elif ":" in dato and "m" in dato[dato.index(":"):] and "://" not in dato:
							return "<type 'time'>"
						elif "https://" in dato or "http://" in dato:
							return "<type 'url'>"
						elif "file://" in dato:
							return "<type 'file'>"
						else:
							return str
					else:
						return type(dato)
				#Estado:finalizado
				#Version:v0.01
			    """ rtype permite corrige el string del tipo de dato"""
			    def rtype(tipo):
					c=str(tipo)
					return c[len("<type '"):-2]
				
				#Estado:finalizado
				#Version:v0.01
			    def id(i):
					self.idseleccion=i
					return self
			    def columna(camp):
					return self.tablas[self.seleccion][self.idseleccion][self.obtenerCampo(camp)]
			    def campo(nombre,tipo,unico=False):
					self.campos[self.seleccion].append([nombre,tipo,unico])
					try:
							if tabla!=None:
								self.registro.append("db('"+tabla+"').campo('"+nombre+"',db."+rtype(tipo)+","+str(unico)+")")
					except:
							self.registro.append("db.campo('"+nombre+"','db."+rtype(tipo)+","+str(unico)+")")
					return self					
                
                #Estado:finalizado
                #Version:v0.01
			    """
			    Esta función permite insertar una lista de campos en la tabla ya seleccionada
			    
			    Ejemplo:
			    		db.insertar('miNombre','miApellido',12345678)
			    """
			    def insertar(*campos):
					c=0
					valido=True
					lcampos=[]
					
					for elem in campos:

						if self.campos[self.seleccion][c][2]==True:
							
							if elem in self.obtenerColumna(self.campos[self.seleccion][c][0]):
								valido=False
							else:
								if self.dbtype(elem)!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
									valido=False
								else:
									lcampos.append(obj(elem))
						
						else:

							if self.dbtype(elem)!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
									valido=False
							else:
									lcampos.append(obj(elem))
		                                
						c+=1
				
					if valido==True:
						self.tablas[self.seleccion][self.clavePrimaria[self.seleccion]]=lcampos
						self.clavePrimaria[self.seleccion]+=1
	                    
						try:
							if tabla!=None:
								self.registro.append("db('"+tabla+"').insertar"+str(campos))
						except:
								self.registro.append("db.insertar"+str(campos))
						if self.debug==True:
							print "La inserción de datos fue realizada con exito"
					else:
						if self.debug==True:
							print "La inserción de datos no puedo ser realizada"
					return self
                        
                #Estado:finalizado
                #Version:v0.01
			    """
			    Esta función permite modificar los valores de los campos de la tabla seleccionada en el id especificado
			    ejemplo:
			    
			    db.modificar() 
			    """
			    def modificarCampo(id,columna,campoNuevo):
					self.tablas[self.seleccion][id][obtenerCampo(columna)].valor=campoNuevo
				
				#Estado: Pendiente
				#Version:v0.01
			    def modificarFila(id,*campos):
					c=0
					for elem in campos:
						for elem2 in self.campos[self.seleccion]:
							if elem2[1]==dbtype(elem):
								if dbtype(elem[1])==self.campos[self.seleccion][c][1]:
									self.tablas[self.seleccion][id][c]=obj(elem)
							c+=1
					try:
							if tabla!=None:
								self.registro.append("db('"+tabla+"').modificar("+str(id)+","+str(campos)[1:-1]+")")
					except:
							self.registro.append("db.modificar("+str(id)+","+str(campos)[1:-1]+")")
					return self				
			    
			    #Estado: Pendiente
			    #Versión: V0.01
			    def grabar(dbfile=self.dbfile):
					f=open(dbfile,"w")
					c=""

					for elem in self.registro:
						c+=elem+"\n"
					f.write(c)
					f.close()
				#Estado: Finalizado
				#Versión: V0.01
			    def obtenerColumna(campo,t=self.seleccion):
					l=[]
					
					for i in self.mostrarTablas()[t]:
						l.append(self.mostrarTablas()[t][i][self.obtenerCampo(campo,t)])
					return l
						
				#Estado: Finalizado
				#Version: V0.01
			    def obtenerCampo(campo,t=self.seleccion):
					c=0
					for elem in self.campos[t]:
						if campo==elem[0]:
							return c
						c+=1
				#Estado: Finalizado
				#Version: v0.01
			    def obtenerFila(campo,t=self.seleccion):
					for elem in self.mostrarTablas(t):
						if campo in self.mostrarTablas(t)[elem]:
							return elem
					
				#Estado: Finalizado
				#Version: v0.01
			    def obtenerCampos(t=self.seleccion):
					c=0
					l=[]
					for elem in self.campos[t]:
							l.append(elem[0])
					return l
								
						
						
				
				#Estado: Finalizado
				#Version: v0.01		
			    def mostrarTablas(mostrar=False,padres=False,seleccion=self.seleccion):
					dtablas={}
					for elem in self.tablas:
						if padres==False:
							dtablas[elem]={}
							for i in self.tablas[elem]:
								dtablas[elem][i]=[]
								for camp in self.tablas[elem][i]:
									dtablas[elem][i].append(camp.valor)

						else:
							if "." not in elem:
								dtablas[elem]={}
								for i in self.tablas[elem]:
									dtablas[elem][i]=[]
									for camp in self.tablas[elem][i]:
										dtablas[elem][i].append(camp.valor)
					
					if mostrar==False:	
						return dtablas
					else:
						return dtablas[seleccion]
				
				#Estado: Finalizado
				#Version: v0.01			
				#tabla1 (i,campo1) <- args["tabla"] (args["id"],args["campo"]) 	
			    def relacionar(i,campo1,**args):
					
					if "id" in args:
						if "campo" in args:
							self.tablas[self.seleccion][i][self.obtenerCampo(campo1)]=self.tablas[args["tabla"]][args["id"]][self.obtenerCampo(args["campo"],args["tabla"])]						
					else:
						self.tablas[self.seleccion][i][self.obtenerCampo(campo1)]=self.tablas[args["tabla"]]
					l=str(args)[1:-1].split(",")	
					c=""
					
					for elem in l:
								c+=elem.split(":")[0][1:-1].replace('"',"").replace("'","")+"="+elem.split(":")[1]+","
												
					try:
							if tabla!=None:
								self.registro.append("db('"+tabla+"').relacionar("+str(i)+",'"+campo1+"',"+c+")")
					except:
							self.registro.append("db.relacionar("+str(i)+",'"+campo1+"',"+c+")")
					return self
                
					
                  
			    self.campo=campo
			    self.insertar=insertar
			    self.str=str
			    self.int=int
			    self.float=float
			    self.bool=bool
			    self.dict=dict
			    self.list=list
			    self.tuple=tuple
			    self.object=object
			    self.all="<type 'all'>"
			    self.email="<type 'email'>"
			    self.time="<type 'time'>"
			    self.date="<type 'date'>"
			    self.datetime="<type 'datetime'>"
			    self.url="<type 'url'>"
			    self.file="<type 'file'>"
			    self.dbtype=dbtype
			    self.modificarFila=modificarFila
			    self.modificarCampo=modificarCampo
			    self.mostrarTablas=mostrarTablas
			    self.grabar=grabar
			    self.obtenerCampo=obtenerCampo
			    self.relacionar=relacionar
			    self.id=id
			    self.debug=debug
			    self.columna=columna
			    self.obtenerCampos=obtenerCampos
			    self.obtenerFila=obtenerFila
			    self.obtenerColumna=obtenerColumna
			    return self
			    
        db.tablas={}
        db.campos={}
        db.clavePrimaria={}
        db.seleccion=None
        db.dbfile=dbfile			
        if dbfile==None:
			db.registro=["from ztec.zdb import DB","db=DB()"]
        else:
			db=dbcargar(dbfile)
         
        
        return db
        

                
        
def dbcargar(dbfile=None):
        if dbfile!=None:
					f=open(dbfile,"r")
					instrucciones=f.read()
					f.close()
					exec(instrucciones)
					return db
	
