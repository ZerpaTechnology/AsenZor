#!/usr/bin/env python
# -*- coding: utf-8 -*-

email="<type 'email'>"
#Estado:
#version:v0.01
"""
la función DB permite crear base de datos de manera sencilla 
"""
class obj:
	def __init__(self,valor,tipo=None):
		self.valor=valor
		self.tipo=tipo
		
def DB(dbfile=None,debug=False):

        def db(tabla=None):
			    self=db
			    self.t=tabla
					
			    def consola(mensaje,d):
					d.log.append(mensaje)
					if d.debug==True:
						print mensaje
			    self.consola=consola
				#nuevo uso del registro, almacena todos los comandos utilizados
				#para que estos luego puedan ser escritos en un archivo aparte
			    if tabla not in self.tablas and tabla not in self.campos:
					self.campos[tabla]=[]
					self.tablas[tabla]={}
					self.clavePrimaria[tabla]=0
					self.log=[]
					self.relaciones={}
			    self.seleccion=tabla


			    self.idseleccion=None
			    #para direfebciar cuando se usa db("tabla")
			    
			    
			    					

				
			    #Estado:finalizado 
			    #version:v0.01
			    """dbtype permite identificar un tipo de dato que pertenece a los tipos de datos que trabaja la base de datos"""
			    def dbtype(dato):
					if type(dato)==str:
						if "@" in dato and ".com" in dato[dato.index("@"):]:
							return "<type 'email'>"
						elif ":" in dato and "://" not in dato:
							t=dato.split(" ")
							if ":" in t[1] and ":" not  in t[0] or ":" in t[0] and ":" not in t[1]:

								if "-" in t[1] and "-" not  in t[0] or "-" in t[0] and "-" not in t[1]:
									return "<type 'datetime'>"
								elif "/" in t[1] and "/" not  in t[0] or "/" in t[0] and "/" not in t[1]:
									return "<type 'datetime'>"
								else:
									return "<type 'date'>"
							else:
									return "<type 'time'>"


						elif "https://" in dato or "http://" in dato:
							return "<type 'url'>"
						elif "file://" in dato:
							return "<type 'file'>"
						else:
							return str
					
					else:
						try:
							return dato.tipo
						except:
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
			    	if self.t!=None:
			    		self.consola(str(self.tablas[self.seleccion][self.idseleccion][self.obtenerCampo(camp)])+"\n",self)
					return self.tablas[self.seleccion][self.idseleccion][self.obtenerCampo(camp)]
			    def campo(nombre,tipo,unico=False,vacio=True,unicaFila=False):
					self.campos[self.seleccion].append([nombre,tipo,unico,vacio,unicaFila])
					try:
							if tabla!=None:
								self.registro.append("db('"+tabla+"').campo('"+nombre+"',db."+rtype(tipo)+","+str(unico)+","+str(vacio)+","+str(unicaFila)+")")
					except:
							self.registro.append("db.campo('"+nombre+"','db."+rtype(tipo)+","+str(unico)+","+str(vacio)+","+str(unicaFila)+")")
					return self					
                
                #Estado:finalizado
                #Version:v0.01
			    """
			    Esta función permite insertar una lista de campos en la tabla ya seleccionada
			    
			    Ejemplo:
			    		db.insertar('miNombre','miApellido',12345678)
			    """
			    def insertar(*campos,**args):
					campos=list(campos)
					valido=True
					if "sob" not in args:
						args["sob"]=False
					lcampos=[]
					razones=[]
					temp=[]
					c=0
					
					for elem in campos:
						
						if self.campos[self.seleccion][c][4]==True:	#unicaFila
							if self.tablas[self.seleccion]!={}:
								if tuple(self.obtenerFilasValores(campos[0],self.seleccion)) == campos:
										valido=False
										break
						c+=1
							
					
									

					

					if valido==True:
						c=0

						for elem in campos:
							
							if self.campos[self.seleccion][c][3]==True:#vacio

								if elem==None:
									lcampos.append(obj(elem,dbtype(elem)))
								else:

									if self.campos[self.seleccion][c][2]==True:#unico

										if args["sob"]==True:

												bloqueados=[]
												for elem2 in self.obtenerColumna(self.obtenerCampos()[c]):

													if self.dbtype(elem)==self.object:

														bloqueados.append(elem2.valor)
												if bloqueados==[]:
													if self.dbtype(elem)!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
														valido=False

														razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem))[1:-1])
													else:
														if self.campos[self.seleccion][c][1]==db.file:
															if self.load==False:
																f=open(elem.replace("file://",""),"rb")
																b=f.read()
																f.close()
																campos[c]="file://"+b
																lcampos.append(obj("file://"+b,dbtype(elem)))
															else:
																lcampos.append(obj(elem.replace("file://",""),dbtype(elem)))
														else:
															lcampos.append(obj(elem,dbtype(elem)))
												else:
													if elem in bloqueados:

														valido=False
														razones.append(str(elem)+" se repite y es un campo unico")
													else:

														if self.campos[self.seleccion][c][1]==db.file:

															if self.load==False:
																f=open(elem.replace("file://",""),"rb")
																b=f.read()
																f.close()
																campos[c]="file://"+b
																lcampos.append(obj("file://"+b,dbtype(elem)))
															else:
																lcampos.append(obj(elem.replace("file://",""),dbtype(elem)))
														else:
															lcampos.append(obj(elem,dbtype(elem)))
														
										else:

											if elem in self.obtenerColumna(self.campos[self.seleccion][c][0]):
												
												valido=False
												razones.append(str(elem)+" se repite y es un campo unico")
											else:
												if self.dbtype(elem)!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
													
													valido=False
													razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem))[1:-1])
												else:

													if self.campos[self.seleccion][c][1]==db.file:
															if self.load==False:
																f=open(elem.replace("file://",""),"rb")
																b=f.read()
																f.close()
																campos[c]="file://"+b
																lcampos.append(obj("file://"+b,dbtype(elem)))
															else:
																lcampos.append(obj(elem.replace("file://",""),dbtype(elem)))
													else:
															lcampos.append(obj(elem,dbtype(elem)))

									else:

										if self.dbtype(elem)!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
												
												valido=False
												#print elem," ",self.campos[self.seleccion][c][0]," ",c,"<br>"
												razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem))[1:-1])
										else:
											
											if self.campos[self.seleccion][c][1]==db.file:

															if self.load==False:
																f=open(elem.replace("file://",""),"rb")
																b=f.read()
																f.close()
																campos[c]="file://"+b

																lcampos.append(obj("file://"+b,dbtype(elem)))

															else:

																lcampos.append(obj(elem.replace("file://",""),dbtype(elem)))
											else:
															lcampos.append(obj(elem,dbtype(elem)))



								
							else:

								if self.campos[self.seleccion][c][2]==True:#unico

									if args["sob"]==True:
											bloqueados=[]
											for elem2 in self.obtenerColumna(self.obtenerCampos()[c]):
												if self.dbtype(elem)==self.object:

													bloqueados.append(elem2.valor)
											if bloqueados==[]:
												if self.dbtype(elem)!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
													valido=False
													razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem))[1:-1])
												else:
														
													lcampos.append(obj(elem,dbtype(elem)))
											else:
												if elem in bloqueados:
													valido=False
													razones.append(str(elem)+" se repite y es un campo unico")
												else:
													lcampos.append(obj(elem,dbtype(elem)))
													
									else:

										if elem in self.obtenerColumna(self.campos[self.seleccion][c][0]):
											valido=False
											razones.append(str(elem)+" se repite y es un campo unico")
										else:
											if self.dbtype(elem)!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
												valido=False
												razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem))[1:-1])
											else:

												if self.campos[self.seleccion][c][1]==db.file:
															if self.load==False:
																f=open(elem.replace("file://",""),"rb")
																b=f.read()
																f.close()
																campos[c]="file://"+b
																lcampos.append(obj("file://"+b,dbtype(elem)))
															else:
																lcampos.append(obj(elem.replace("file://",""),dbtype(elem)))
												else:
															lcampos.append(obj(elem,dbtype(elem)))

								else:

									if self.dbtype(elem)!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
											valido=False
											razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem))[1:-1])
									else:

										if self.campos[self.seleccion][c][1]==db.file:
															if self.load==False:
																f=open(elem.replace("file://",""),"rb")
																b=f.read()
																f.close()
																campos[c]="file://"+b
																lcampos.append(obj("file://"+b,dbtype(elem)))
															else:
																lcampos.append(obj(elem.replace("file://",""),dbtype(elem)))
										else:
															lcampos.append(obj(elem,dbtype(elem)))
				                                
							c+=1
					
					if valido==True:
						self.tablas[self.seleccion][self.clavePrimaria[self.seleccion]]=lcampos
						self.clavePrimaria[self.seleccion]+=1

						try:
							if tabla!=None:
								self.registro.append("db('"+tabla+"').insertar("+str(campos)[1:-1]+")")
								self.consola("La inserción de datos fue realizada con exito en la tabla \n \x1b[1;31m "+self.seleccion+"\n Datos insertados:\n"+str(campos)+" \x1b[0m\n",self)
						except:
								self.registro.append("db.insertar("+str(campos)[1:-1]+")")
								self.consola("La inserción de datos fue realizada con exito en la tabla \x1b[1;31m"+self.seleccion+"\x1b[0m \n Datos insertados:\n"+str(campos)+"\n",self)
							
					else:
					
							self.consola("La inserción de datos no puedo ser realizada en la tabla \x1b[1;31m"+self.seleccion+"\x1b[0m .\nRazones: \n "+str(razones)+"\n",self)
					
					return self
                        
                #Estado:finalizado
                #Version:v0.01
			    """
			    Esta función permite modificar los valores de los campos de la tabla seleccionada en el id especificado
			    ejemplo:
			    
			    db.modificar() 
			    """

			    def modificarCampo(i,columna,campoNuevo,tabla=self.seleccion):#columna es el nombre del campo
					col=obtenerCampo(columna)
					self.consola("modificarFila\n de: "+str(self.tablas[self.seleccion][i][self.obtenerCampo(columna)].valor)+" a: "+str(campoNuevo)+"\n",self)
					old=self.obtenerFilaValores(i,tabla)[col]


					c=0
					self.modificaciones={}
					ri1=0
					ri2=0
					for elem in self.registro:
	
						if tabla in self.relaciones:
								i1,campo1,tabla2,i2,campo2=self.relaciones[tabla]
								i2,campo2,tabla1,i1,campo1=self.relaciones[tabla2]
								
								if columna==campo1:
									if "db('"+tabla2+"').insertar(" in elem:
										if ri2==i2:
											
											fila=self.obtenerFilaValores(i2,tabla2)
											
											col2=self.obtenerCampo(campo2,tabla2)
											fila[col2]=campoNuevo
				
											self.modificaciones[c]="db('"+tabla2+"').insertar("+str(fila)[1:-1]+")"
										ri2+=1
									if "db('"+tabla1+"').insertar(" in elem:
										if ri1==i1 and ri1==i:
											
											fila=self.obtenerFilaValores(i1,tabla1)
											
											col2=self.obtenerCampo(campo1,tabla1)
											
											fila[col2]=campoNuevo
											

											self.modificaciones[c]="db('"+tabla1+"').insertar("+str(fila)[1:-1]+")"
										ri1+=1
								else:
									if "db('"+tabla+"').insertar("+str(self.obtenerFilaValores(i,tabla))[1:-1]+")" == elem:

										#print "se ha modificado ", self.registro[c]
										fila=self.obtenerFilaValores(i,tabla)
										fila[col]=campoNuevo
										params=str(fila)[1:-1]

										self.modificaciones[c]="db('"+tabla+"').insertar("+params+")"


								"""
								if "db('"+tabla2+"').insertar("+str(fila)[1:-1]+")" == elem:
									
									
									self.modificaciones[c]="db('"+tabla2+"').insertar("+str(fila)[1:-1]+")"
								"""
						else:
							if "db('"+tabla+"').insertar("+str(self.obtenerFilaValores(i,tabla))[1:-1]+")" == elem:

								#print "se ha modificado ", self.registro[c]
								fila=self.obtenerFilaValores(i,tabla)
								fila[col]=campoNuevo
								params=str(fila)[1:-1]

								self.modificaciones[c]="db('"+tabla+"').insertar("+params+")"





									



							

						c+=1
					print self.modificaciones
					for elem in self.modificaciones:
						self.registro[elem]=self.modificaciones[elem]
					self.tablas[self.seleccion][i][col].valor=campoNuevo



			    def delFila(i,tabla=self.seleccion):
					c=0
					ids=0

					for elem in self.registro:
						if "db('"+tabla+"').insertar(" in elem:
							print "se ha eliminado ", self.registro[c]
							if ids==i:
								del self.registro[c]
							ids+=1
						elif "tabla="+tabla in elem[elem.find("').relacionar(") :] and "id="+str(i) in elem[elem.find("').relacionar(") :]:
							print "se ha eliminado ", self.registro[c]
							del self.registro[c]
						c+=1

				#Estado: Pendiente
				#Version:v0.01
			    def modificarFila(id,*campos):
					c=0
					for elem in campos:
						for elem2 in self.campos[self.seleccion]:
							if elem2[1]==dbtype(elem):
								if dbtype(elem[1])==self.campos[self.seleccion][c][1]:

									self.consola("modificarFila\n de: "+str(self.tablas[self.seleccion][id][c])+" a: "+str(obj(elem,dbtype(elem)))+"\n",self)
									self.tablas[self.seleccion][id][c]=obj(elem,dbtype(elem))
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
					self.registro.insert(3,"db.load=True")
					self.registro.append("db.load=False")
					f=open(dbfile,"w")
					c=""

					for elem in self.registro:
						c+=elem+"\n"
					f.write(c)
					f.close()
					self.consola("La base de datos fue grabada con exito\n",self)
				#Estado: Finalizado
				#Versión: V0.01
			    def obtenerColumna(campo,t=self.seleccion,self=self):
					l=[]
					for i in self.mostrarTablas()[t]:
						l.append(self.mostrarTablas()[t][i][self.obtenerCampo(campo,t)])
					if self.t!=None:
						self.consola("obtenerColumna "+self.t+"\n"+str(l)+"\n",self)
					return l
						
				#Estado: Finalizado
				#Version: V0.01
			    #retorna la posicion de la primera fila que conicida en valor de campo 
			    def obtenerCampo(campo,t=self.seleccion):
					c=0
					for elem in self.campos[t]:
						if campo==elem[0]:
							if self.t!=None:
								self.consola("obtenerCampo\n"+str(c)+"\n",self)
							return c
						c+=1
				#Estado: Finalizado
				#Version: v0.01
				#retorna los id's de las filas donde se encuentra el campo 
			    def obtenerFilasId(campo,t=self.seleccion):
					l=[]
					
					for elem in self.mostrarTablas()[t]:
						if campo in self.mostrarTablas()[t][elem]:
							
							l.append(elem)

					if self.t!=None:
						self.consola("obtenerFila\n"+str(elem)+"\n",self)

					return l
			    
			    def obtenerFilas(campo,t=self.seleccion):
					l=obtenerFilasId(campo,t)
					
					l2=[]
					for i in l:
						l2.append(self.tablas[t][i])
					return l2

			    
			    def obtenerFilasValores(campo,t=self.seleccion):
					l=obtenerFilas(campo,t)
					l2=[]
					
					for fila in l:

						for o in fila:
							
							l2.append(o.valor)
					return l2
				
			    def obtener(i,campo,t=self.seleccion):
			    	
			    	return self.tablas[t][i][obtenerCampo(campo,t)].valor

			    def obtenerFilaValores(i,t=self.seleccion):
			    	l=[]
			    	for elem in self.tablas[t][i]:
			    		l.append(elem.valor)
			    	return l


				#Estado: Finalizado
				#Version: v0.01
				#retorna los nombres de los campos de la tabla
			    def obtenerCampos(t=self.seleccion):
					c=0
					l=[]
					for elem in self.campos[t]:
							l.append(elem[0])
					if self.t!=None:
						self.consola("obtenerCampos\n"+str(l)+"\n",self)
					return l

								
						
						
				
				#Estado: Finalizado
				#Version: v0.01		
				#Muestra las tablas de la base de datos, si se le pasa seleccion esta retorna la tabla especificada
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
							if self.tablas[args["tabla"]][args["id"]][self.obtenerCampo(args["campo"],args["tabla"])].tipo==self.object:	
									
									self.consola("Ya existe una relación para este campo\n",self)

							else:
								self.tablas[args["tabla"]][args["id"]][self.obtenerCampo(args["campo"],args["tabla"])].tipo=self.object
								
								self.tablas[self.seleccion][i][self.obtenerCampo(campo1)]=self.tablas[args["tabla"]][args["id"]][self.obtenerCampo(args["campo"],args["tabla"])]									
								l=str(args)[1:-1].split(",")	
								c=""
								
								for elem in l:
											c+=elem.split(":")[0][1:-1].replace('"',"").replace("'","")+"="+elem.split(":")[1]+","
															
								try:
										if tabla!=None:
											self.registro.append("db('"+tabla+"').relacionar("+str(i)+",'"+campo1+"',"+c+")")
											#nuevo
											#self.campos[self.seleccion][self.obtenerCampos(args["tabla"]).index(args["campo"])][1]=self.object
											self.consola("La relación fue efectuada con exito\n",self)
											self.relaciones[self.seleccion]=[i,campo1,args["tabla"],args["id"],args["campo"]]
												
								except:
										self.registro.append("db.relacionar("+str(i)+",'"+campo1+"',"+c+")")
										#nuevo
										#self.campos[self.seleccion][self.obtenerCampos(args["tabla"]).index(args["campo"])][1]=self.object
										self.consola("La relación fue efectuada con exito\n",self)
										self.relaciones[self.seleccion]=[i,campo1,args["tabla"],args["id"],args["campo"]]


					else:
						if self.tablas[args["tabla"]].tipo==self.object:
									self.consola("Ya existe una relacion para este campo\n",self)
						else:
							self.tablas[self.seleccion][i][self.obtenerCampo(campo1)]=self.tablas[args["tabla"]]		
							l=str(args)[1:-1].split(",")	
							c=""
							
							for elem in l:
										c+=elem.split(":")[0][1:-1].replace('"',"").replace("'","")+"="+elem.split(":")[1]+","
														
							try:
									if tabla!=None:
										self.registro.append("db('"+tabla+"').relacionar("+str(i)+",'"+campo1+"',"+c+")")	
										self.consola("La relación fue efectuada con exito\n")
										self.relaciones[self.seleccion]=[i,campo1,args["tabla"],args["id"],args["campo"]]
							except:
									self.registro.append("db.relacionar("+str(i)+",'"+campo1+"',"+c+")")
									self.relaciones[self.seleccion]=[i,campo1,args["tabla"],args["id"],args["campo"]]

									self.consola("La relación fue efectuada con exito\n",self)
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
			    self.bin="<type 'binary'>"
			    self.dbtype=dbtype
			    self.modificarFila=modificarFila
			    self.modificarCampo=modificarCampo
			    self.mostrarTablas=mostrarTablas
			    self.grabar=grabar
			    self.obtenerCampo=obtenerCampo
			    self.relacionar=relacionar
			    self.id=id
			    self.consola=consola
			    self.debug=debug
			    self.columna=columna
			    self.obtenerCampos=obtenerCampos
			    self.obtenerFilas=obtenerFilas
			    self.obtenerFilasId=obtenerFilasId
			    self.obtenerFilasValores=obtenerFilasValores
			    self.obtenerFilaValores=obtenerFilaValores
			    self.obtenerColumna=obtenerColumna
			    self.obtener=obtener
			    self.delFila=delFila
			    self.t=None
			    

			    return self
			    
        db.tablas={}
        db.campos={}
        db.clavePrimaria={}
        db.seleccion=None
        db.dbfile=dbfile
        db.log=[]
        db.load=False
        db.modificacion=False

        
    		
        if dbfile==None:
			db.registro=["# -*- coding: utf-8 -*-","from ztec.zdb import DB","db=DB()"]
        else:
			x=dbcargar(dbfile,debug)
			if x==None:
				db.log.append("Ocurrio un error al cargar la base de datos\n")
			else:
				db=x
        return db
        

                
        
def dbcargar(dbfile=None,debug=False):
        if dbfile!=None:
					f=open(dbfile,"r")
					instrucciones=f.read()
					f.close()
					try:
						exec(instrucciones)
						db.debug=debug
						db.consola("--------------------------------------------\nLa base de datos fue cargada con exito\n",db)
						db.t=None
						db.registro.append("db.load=True")

						return db
					except Exception,e:
						if debug==True:
							print "ocurrio un error al cargar la base de datos"
							print e
						

	
