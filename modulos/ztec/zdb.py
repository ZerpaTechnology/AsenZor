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
					self.nmodif=0
					
					self.lrelaciones=[]

					
					self.relaciones={}
			    self.seleccion=tabla


			    self.idseleccion=None
			    #para direfebciar cuando se usa db("tabla")
			    
			    
			    					

				
			    #Estado:finalizado 
			    #version:v0.01
			    """dbtype permite identificar un tipo de dato que pertenece a los tipos de datos que trabaja la base de datos"""
			    def dbtype(dato,formato=None):
			    	try:
						if type(dato)==str:
							if "mailto:"==dato[:len("mailto:")] and "@" in dato and (".com" in dato[dato.index("@"):] or ".org" in dato[dato.index("@"):] or ".net" in dato[dato.index("@"):]):
								return "<type 'email'>"
							elif "date:"==dato[:len("date:")]:
								if formato!=None:
									try:
										data=dato[len("date:"):]
										sp=formato.replace("%d","").replace("%m","").replace("%y","")[0]
										if sp in data:
											for elem in data.split(sp):
												try:
													int(elem)
												except:
													return None
										return "<type 'date'>"
									except Exception,e:
										print "Error en dbtype -> date"
										print e
								else:
									print "Hace falta formato para ",dato
									return None

							elif "datetime:"==dato[:len("datetime:")]:
								if formato!=None:
									try:
											data=dato[len("datetime:"):]
											
											if " - " in data and " - " in formato and formato.count(" - ")==1:
												parts=data.split(" - ")
												fparts=formato.split(" - ")
												if dbtype(parts[0],fparts[0])=="<type 'date'>" and dbtype(parts[1],fparts[1])=="<type 'time'>":
													return "<type 'datetime'>"
												elif dbtype(parts[1],fparts[1])=="<type 'date'>" and dbtype(parts[0],fparts[0])=="<type 'time'>":
													return "<type 'datetime'>"
											elif " " in data and " " in formato and formato.count(" ")==1:
												
												parts=data.split(" ")
												fparts=formato.split(" ")
												

												if dbtype("date:"+parts[0],fparts[0])=="<type 'date'>" and dbtype("time:"+parts[1],fparts[1])=="<type 'time'>":
													return "<type 'datetime'>"
												elif dbtype("date:"+parts[1],fparts[1])=="<type 'date'>" and dbtype("time:"+parts[0],fparts[0])=="<type 'time'>":
													return "<type 'datetime'>"
											else:
												return None
											

										

									except Exception,e:
										print "error en dbtype -> datetime<br>"
										print e
								else:
									print "Hace falta formato para ",dato

									
							
							elif "time:"==dato[:len("time:")]:
								if formato!=None:
									try:
										data=dato[len("time:"):]
										if "%H" in formato and "%M" in formato and "%S" in formato:
											sp=formato.replace("%H","").replace("%M","").replace("%S","")[0]
											for elem in data.split(sp):
												try:
													if elem !="":
														int(elem)
												except:
													return None
											return "<type 'time'>"

										elif "%H" in formato and "%M" in formato and "%S" not in formato:
											sp=formato.replace("%H","").replace("%M","")[0]

											for elem in data.split(sp):
												
												try:
													if elem !="":
														int(elem)
												except:
													return None
											return "<type 'time'>"
										elif "%I" in formato and "%M" in formato and "%S" in formato:
											sp=formato.replace("%I","").replace("%M","").replace("%S","")[0]
											for elem in data.split(sp):
												try:
													if elem !="":
														int(elem)
												except:
													return None
											return "<type 'time'>"
										elif "%I" in formato and "%M" in formato and "%S" not in formato:
											sp=formato.replace("%I","").replace("%M","")[0]
											for elem in data.split(sp):
												try:
													if elem !="":
														int(elem)
												except:
													return None
											return "<type 'time'>"
										
										elif "%I" not in formato and "%H" not in formato and "%M" in formato and "%S" in formato:
											sp=formato.replace("%M","").replace("%S","")[0]
											for elem in data.split(sp):
												try:
													if elem !="":
														int(elem)
												except:
													return None
											return "<type 'time'>"
										elif "%I" not in formato and "%H" not in formato and "%M" not in formato and "%S" in formato:
											try:
												if elem !="":
														int(data)
											except:
												return None
											return "<type 'time'>"
										elif "%I" not in formato and "%H" not in formato and "%M" in formato and "%S" not in formato:
											try:
												if elem !="":
														int(data)
											except:
												return None
											return "<type 'time'>"
										else:
											return None

									except Exception,e:
										print "Error en dbtype -> time"
										print e
									
								else:
									print "Hace falta formato para ",dato


							elif "https://" == dato[:len("https://")] or "http://" == dato[:len("http://")] or "ftp://" == dato[:len("ftp://") or "news://" == dato[:len("news://")]] or "telnet://" == dato[:len("telnet://")]:
								return "<type 'url'>"

							elif "data:" == dato[:len("data:")]:
								return "<type 'binary'>"

							elif "password:" == dato[:len("password:")]:
								return "<type 'password'>"
								
							elif "ldap:" == dato[:len("ldap:")]:
								return "<type 'serverFolder'>"

							elif "file://" == dato[:len("file://")]:
								return "<type 'file'>"
							else:
								if len(dato)>= 70:
									return "<type 'doc'>"
								else:
									return str
						
						else:
							try:
								return dato.tipo
							except:
								return type(dato)


			    	except Exception, e:
			    		print "error en dbtype <br>"								
			    		print e

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
			    	print self.idseleccion
			    	if self.t!=None:
			    		self.consola(str(self.tablas[self.seleccion][self.idseleccion][self.obtenerCampo(camp)])+"\n",self)
					return self.tablas[self.seleccion][self.idseleccion][self.obtenerCampo(camp)]

			    def campo(nombre,tipo,unico=False,vacio=True,unicaFila=False,unicacolumna=False,mini=0,maxi=-1,step=None,formato=None):
					try:
							self.campos[self.seleccion].append([nombre,tipo,unico,vacio,unicaFila,unicacolumna,mini,maxi,step,formato])
							if tabla!=None:
								if type(formato)==str:
									formato="'"+formato+"'"
								self.registro.append("db('"+tabla+"').campo('"+nombre+"',db."+rtype(tipo)+","+str(unico)+","+str(vacio)+","+str(unicaFila)+","+str(unicacolumna)+","+str(mini)+","+str(maxi)+","+str(step)+","+str(formato)+")")
								self.rcampos.append("db('"+tabla+"').campo('"+nombre+"',db."+rtype(tipo)+","+str(unico)+","+str(vacio)+","+str(unicaFila)+","+str(unicacolumna)+","+str(mini)+","+str(maxi)+","+str(step)+","+str(formato)+")")
								
					except Exception as e:
							print ""
							print "error al crear campos"
							print e
							self.registro.append("db.campo('"+nombre+"','db."+rtype(tipo)+","+str(unico)+","+str(vacio)+","+str(unicaFila)+","+str(unicacolumna)+","+str(mini)+","+str(maxi)+","+str(step)+","+str(formato)+")")
							self.rcampos.append("db.campo('"+nombre+"','db."+rtype(tipo)+","+str(unico)+","+str(vacio)+","+str(unicaFila)+","+str(unicacolumna)+","+str(mini)+","+str(maxi)+","+str(step)+","+str(formato)+")")
				
					return self					
                
                #Estado:finalizado
                #Version:v0.01
			    """
			    Esta función permite insertar una lista de campos en la tabla ya seleccionada
			    
			    Ejemplo:
			    		db.insertar('miNombre','miApellido',12345678)
			    """
			    def insertar(*campos,**args):
			    	
			    	try:
						campos=list(campos)
						valido=True
						if "sob" not in args:
							args["sob"]=False
						lcampos=[]
						razones=[]
						temp=[]
						c=0
						
						for elem in campos:
							if self.campos[self.seleccion][c][5]==True: #unicacolumna
								if campos.count(elem)>1:
									valido=False
									break
							if self.campos[self.seleccion][c][4]==True:	#unicaFila
								if self.tablas[self.seleccion]!={}:
									if tuple(self.obtenerFilasValores(campos[0],self.seleccion)) == campos:
											valido=False
											break
							c+=1
								
						
										

						

						if valido==True:
							c=0

							for elem in campos:
								try:
									if self.campos[self.seleccion][c][3]==True:#vacio
										try:
											if elem==None:
												lcampos.append(obj(elem,self.dbtype(elem,self.campos[self.seleccion][c][9]) ))
											else:

												if self.campos[self.seleccion][c][2]==True:#unico
													try:

														if args["sob"]==True:
															try:

																bloqueados=[]
																for elem2 in self.obtenerColumna(self.obtenerCampos()[c]):

																	if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.object:

																		bloqueados.append(elem2.valor)
																if bloqueados==[]:
																	try:
																		if self.dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
																			if self.campos[self.seleccion][c][1]==self.doc and self.dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																				lcampos.append(obj(elem,self.doc))
																			else:
																				valido=False
																				razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1])
																		else:
																			if self.campos[self.seleccion][c][1]==db.file:
																				if self.load==False:
																					f=open(elem.replace("file://",""),"rb")
																					b=f.read()
																					f.close()
																					campos[c]="file://"+b
																					if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																							if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																									lcampos.append(obj("file://"+b,self.dbtype(elem,self.campos[self.seleccion][c][9]) ))
																							else:
																									valido=False
																									razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																						
																						if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj("file://"+b,self.dbtype(elem,self.campos[self.seleccion][c][9]) ))
																						else:
																							valido=False
																							razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																						lcampos.append(obj("file://"+b,self.dbtype(elem,self.campos[self.seleccion][c][9]) ))
																					else:
																						valido=False
																						razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")
																				else:
																					lcampos.append(obj(elem.replace("file://",""),self.dbtype(elem,self.campos[self.seleccion][c][9]) ))
																			else:
																				if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																					if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.int or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.float or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																						if elem>=self.campos[self.seleccion][c][6]:
																							lcampos.append(obj(elem,self.dbtype(elem,self.campos[self.seleccion][c][9]) ))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																					else:
																						if len(elem)>=self.campos[self.seleccion][c][6]:

																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																				elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																					if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.int or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.float or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																						if elem>=self.campos[self.seleccion][c][6] and elem<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																					else:	
																						if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																				elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																					lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																					valido=False
																					razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																
																	except Exception as e:
																		print "Error en el bloque vacio -> unico : nobloqueados "
																		print e
																else:
																	try:

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
																					if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																							if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																									lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																									valido=False
																									razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																						
																						if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																						lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																					else:
																						valido=False
																						razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")
																				else:
																					lcampos.append(obj(elem.replace("file://",""),dbtype(elem,self.campos[self.seleccion][c][9])))
																			else:
																				if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																					if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.int or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.float or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																						if elem>=self.campos[self.seleccion][c][6]:
																							lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																					else:
																						if len(elem)>=self.campos[self.seleccion][c][6]:

																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																				elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																					if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.int or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.float or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																						if elem>=self.campos[self.seleccion][c][6] and elem<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																					else:	
																						if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																				elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																					lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																					valido=False
																					razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																			
																	except Exception as e:															
																		print "Error en el bloque vacio -> unico sobrescribir : bloqueados "
																		print e

														
															except Exception as e:
																print "Error en el bloque vacio -> unico sobrescribir : bloqueados "
																print e
														else:
															try:

																if elem in self.obtenerColumna(self.campos[self.seleccion][c][0]):
																	
																	valido=False
																	razones.append(str(elem)+" se repite y es un campo unico")
																else:
																	if self.dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
																		if self.campos[self.seleccion][c][1]==self.doc and self.dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																			if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																				if len(elem)>=self.campos[self.seleccion][c][6]:
																					lcampos.append(obj(elem,self.doc))
																				else:
																					valido=False
																					razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																			elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																				
																				if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																					lcampos.append(obj(elem,self.doc))
																				else:
																					valido=False
																					razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																			elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																				lcampos.append(obj(elem,self.doc))
																			else:
																				valido=False
																				razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																		else:
																			valido=False
																			razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1])
																	else:

																		if self.campos[self.seleccion][c][1]==db.file:
																				if self.load==False:
																					f=open(elem.replace("file://",""),"rb")
																					b=f.read()
																					f.close()
																					campos[c]="file://"+b
																					if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																							if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																									lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																									valido=False
																									razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																						
																						if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																						lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																					else:
																						valido=False
																						razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")
																				else:
																					lcampos.append(obj(elem.replace("file://",""),dbtype(elem,self.campos[self.seleccion][c][9])))
																		else:
																				if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																					if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.int or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.float or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																						if elem>=self.campos[self.seleccion][c][6]:
																							lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																					else:
																						if len(elem)>=self.campos[self.seleccion][c][6]:

																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																				elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																					if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.int or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.float or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																						if elem>=self.campos[self.seleccion][c][6] and elem<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																					else:	
																						if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																				elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																					lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																					valido=False
																					razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

															except Exception as e:
																print "Error en el bloque vacio -> unico nosobrescribir : bloqueados "
																print e													

													except Exception as e:
														print "Error en bloque vacio -> unico "
														print e
												else:
													try:
														

														if self.dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
															
															
															if self.campos[self.seleccion][c][1]==self.doc and self.dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																
																try:



																	if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:

																		if len(elem)>=self.campos[self.seleccion][c][6]:
																			lcampos.append(obj(elem,self.doc))
																		else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																	elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																		
																		if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																			lcampos.append(obj(elem,self.doc))
																		else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																	elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:

																		lcampos.append(obj(elem,self.doc))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
															
																except Exception as e:
																	print "Error en bloque vacio -> no-unico -> tipo igual -> tipo doc <br>"
															else:
																valido=False
																#print elem," ",self.campos[self.seleccion][c][0]," ",c,"<br>"
																razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1])


														else:
															try:

																if self.campos[self.seleccion][c][1]==db.file:

																				if self.load==False:
																					f=open(elem.replace("file://",""),"rb")
																					b=f.read()
																					f.close()
																					campos[c]="file://"+b

																					if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																							if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																									lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																									valido=False
																									razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																						
																						if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																						lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																					else:
																						valido=False
																						razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")


																				else:

																					lcampos.append(obj(elem.replace("file://",""),dbtype(elem,self.campos[self.seleccion][c][9])))
																else:
																				
																				if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																					if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.int or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.float or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																						if elem>=self.campos[self.seleccion][c][6]:
																							lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																					else:
																						if len(elem)>=self.campos[self.seleccion][c][6]:

																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																				elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																					if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.int or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.float or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																						if elem>=self.campos[self.seleccion][c][6] and elem<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																					else:	
																						if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																							lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																				elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:

																					lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																					valido=False
																					razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
															except Exception as e:
																print "Error en bloque vacio -> no-unico -> tipo igual <br>"
																print e


													except Exception as e:
														print "Error en bloque vacio -> no-unico <br>"
														print e
										except Exception as e:
											print "Error en bloque vacio "
											print e
										
									else:

										if self.campos[self.seleccion][c][2]==True:#unico

											if args["sob"]==True:
													bloqueados=[]
													for elem2 in self.obtenerColumna(self.obtenerCampos()[c]):
														if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.object:

															bloqueados.append(elem2.valor)
													if bloqueados==[]:
														if self.dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
															if self.campos[self.seleccion][c][1]==self.doc and self.dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																	if len(elem)>=self.campos[self.seleccion][c][6]:
																		lcampos.append(obj(elem,self.doc))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																	
																	if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																		lcampos.append(obj(elem,self.doc))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																	lcampos.append(obj(elem,self.doc))
																else:
																	valido=False
																	razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
															else:
																valido=False
																razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1])
														else:
																
															if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																if len(elem)>=self.campos[self.seleccion][c][6]:
																		lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

															elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																
																if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																	lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																else:
																	valido=False
																	razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

															elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
															else:
																valido=False
																razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
													else:
														if elem in bloqueados:
															valido=False
															razones.append(str(elem)+" se repite y es un campo unico")
														else:
															if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																if len(elem)>=self.campos[self.seleccion][c][6]:
																		lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

															elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																
																if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																	lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																else:
																	valido=False
																	razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

															elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
															else:
																valido=False
																razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
															
											else:

												if elem in self.obtenerColumna(self.campos[self.seleccion][c][0]):
													valido=False
													razones.append(str(elem)+" se repite y es un campo unico")
												else:
													if self.dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
														if self.campos[self.seleccion][c][1]==self.doc and self.dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																	if len(elem)>=self.campos[self.seleccion][c][6]:
																		lcampos.append(obj(elem,self.doc))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																	
																	if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																		lcampos.append(obj(elem,self.doc))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																	lcampos.append(obj(elem,self.doc))
																else:
																	valido=False
																	razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
														else:
															valido=False
															razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1])
													else:

														if self.campos[self.seleccion][c][1]==db.file:
																	if self.load==False:
																		f=open(elem.replace("file://",""),"rb")
																		b=f.read()
																		f.close()
																		campos[c]="file://"+b
																		if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																				if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																						lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																						valido=False
																						razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																		elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																			
																			if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																				lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																			else:
																				valido=False
																				razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																		elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																			lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																		else:
																			valido=False
																			razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")
																	else:
																		lcampos.append(obj(elem.replace("file://",""),dbtype(elem,self.campos[self.seleccion][c][9])))
														else:
																	if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																		if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.int or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.float or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																			if elem>=self.campos[self.seleccion][c][6]:
																				lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																			else:
																				valido=False
																				razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																		else:
																			if len(elem)>=self.campos[self.seleccion][c][6]:

																					lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																			else:
																					valido=False
																					razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																	elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																		if self.dbtype(elem,self.campos[self.seleccion][c][9])==self.int or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.float or self.dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																			if elem>=self.campos[self.seleccion][c][6] and elem<=self.campos[self.seleccion][c][7]:
																				lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																			else:
																				valido=False
																				razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																		else:	
																			if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																				lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																			else:
																				valido=False
																				razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																	elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																		lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

										else:

											if self.dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
													if self.campos[self.seleccion][c][1]==self.doc and self.dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																	if len(elem)>=self.campos[self.seleccion][c][6]:
																		lcampos.append(obj(elem,self.doc))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																	
																	if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																		lcampos.append(obj(elem,self.doc))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																	lcampos.append(obj(elem,self.doc))
																else:
																	valido=False
																	razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
													else:
														valido=False
														razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(self.dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1])
											else:

												if self.campos[self.seleccion][c][1]==db.file:
																	if self.load==False:
																		f=open(elem.replace("file://",""),"rb")
																		b=f.read()
																		f.close()
																		campos[c]="file://"+b
																		if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																				if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																						lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																						valido=False
																						razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																		elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																			
																			if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																				lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																			else:
																				valido=False
																				razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																		elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																			lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																		else:
																			valido=False
																			razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")
																	else:
																		lcampos.append(obj(elem.replace("file://",""),dbtype(elem,self.campos[self.seleccion][c][9])))
												else:
													if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																if len(elem)>=self.campos[self.seleccion][c][6]:
																		lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

													elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
														
														if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
															lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
														else:
															valido=False
															razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

													elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
														lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
													else:
														valido=False
														razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																	
								except Exception as e:
									print "Error en bloque Principal"						                                
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
			    	except Exception, e:
						print "Error al insertar "
						print e
                        
                #Estado:finalizado
                #Version:v0.01
			    """
			    Esta función permite modificar los valores de los campos de la tabla seleccionada en el id especificado
			    ejemplo:
			    
			    db.modificar() 
			    """

			    def modificarCampo(i,columna,campoNuevo,tabla=self.seleccion):#columna es el nombre del campo
					
					if obtenerCampo(columna)!=None:
						self.tablas[self.seleccion][i][obtenerCampo(columna)].valor=campoNuevo
						self.registro.append("db('"+tabla+"').modificarCampo("+str(i)+",'"+columna+"',"+("'"+campoNuevo+"'" if type(campoNuevo)==str else str(campoNuevo))+")")
						#print "nmodif ", self.nmodif
						self.nmodif+=1
						
					else:
						print "esta columna "+columna+" no existe en la tabla"

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
							if elem2[1]==dbtype(elem,self.campos[self.seleccion][c][8]):
								if dbtype(elem[1],self.campos[self.seleccion][c][8])==self.campos[self.seleccion][c][1]:

									self.consola("modificarFila\n de: "+str(self.tablas[self.seleccion][id][c])+" a: "+str(obj(elem,dbtype(elem,self.campos[self.seleccion][c][8])))+"\n",self)
									self.tablas[self.seleccion][id][c]=obj(elem,dbtype(elem,self.campos[self.seleccion][c][8]))
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
					clear()
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
				#retorna una columna con todos los valores de la columna que forma el campo pasando el nombre del campo como parametro
			    def obtenerColumna(campo,t=self.seleccion):
					l=[]
					for i in self.mostrarTablas()[t]:
						l.append(self.mostrarTablas()[t][i][self.obtenerCampo(campo,t)])
					if self.t!=None:
						self.consola("obtenerColumna "+self.t+"\n"+str(l)+"\n",self)
					return l
						
				#Estado: Finalizado
				#Version: V0.01
			    #retorna la posicion de la primera fila que conicida en nombre del campo 
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
							if type(o.valor)==str:
								if "mailto:" in o.valor and o.valor[:len("mailto:")]=="mailto:":
									l2.append(o.valor[len("mailto:"):])
								elif "password:" in o.valor and o.valor[:len("password:")]=="password:":
									l2.append(o.valor[len("password:"):])
								elif "datetime:" in o.valor and o.valor[:len("datetime:")]=="datetime:":
									l2.append(o.valor[len("datetime:"):])
								elif "date:" in o.valor and o.valor[:len("date:")]=="date:":
									l2.append(o.valor[len("date:"):])
								elif "time:" in o.valor and o.valor[:len("time:")]=="time:":
									l2.append(o.valor[len("time:"):])

								else:
									l2.append(o.valor)
							else:
								l2.append(o.valor)
					return l2
			    def obtenerFilasValoresPuro(campo,t=self.seleccion):
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
		    			if type(elem.valor)==str:
							if "mailto:" in elem.valor and elem.valor[:len("mailto:")]=="mailto:":
								l.append(elem.valor[len("mailto:"):])
							elif "password:" in elem.valor and elem.valor[:len("password:")]=="password:":
								l.append(elem.valor[len("password:"):])
							elif "datetime:" in elem.valor and elem.valor[:len("datetime:")]=="datetime:":
								l.append(elem.valor[len("datetime:"):])
							elif "date:" in elem.valor and elem.valor[:len("date:")]=="date:":
								l.append(elem.valor[len("date:"):])
							elif "time:" in elem.valor and elem.valor[:len("time:")]=="time:":
								l.append(elem.valor[len("time:"):])

							else:
								l.append(elem.valor)
		    			else:
							l.append(elem.valor)
		    	
			    	return l


			    def obtenerFilaValoresPuro(i,t=self.seleccion):
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
				
			    def clear():
			    	
			    	if self.nmodif>=self.limite:
			    		
				    	
				    	l=[]
				    	l2=self.rcampos
				    	for tabla in self.tablas:
				    		
				    		for i in self.tablas[tabla]:

				    			l.append("db('"+tabla+"').insertar("+str(obtenerFilaValoresPuro(i,tabla))[1:-1]+")")
				    	l2.extend(l)
				    	l2.extend(self.lrelaciones)
				    	
				    	self.registro=l2
				    	#self.registro.append("db.load=False")
				    	self.nmodif=0

			    			






				#Estado: Finalizado
				#Version: v0.01			
				#tabla1 (i,campo1) <- args["tabla"] (args["id"],args["campo"]) 	

			    def relacionar(i,campo1,**args):

					try:

						if self.obtenerCampo(args["campo"],args["tabla"])!=None:
							
							if "id" in args:
								if "campo" in args:
									try:
										if self.tablas[args["tabla"]][args["id"]][self.obtenerCampo(args["campo"],args["tabla"])].tipo==self.object:	
												
												self.consola("Ya existe una relación para este campo\n",self)

										else:
											try:

												self.tablas[args["tabla"]][args["id"]][self.obtenerCampo(args["campo"],args["tabla"])].tipo=self.object
												
												self.tablas[self.seleccion][i][self.obtenerCampo(campo1)]=self.tablas[args["tabla"]][args["id"]][self.obtenerCampo(args["campo"],args["tabla"])]									
												l=str(args)[1:-1].split(",")	
												c=""
												
												for elem in l:
															c+=elem.split(":")[0][1:-1].replace('"',"").replace("'","")+"="+elem.split(":")[1]+","
																		
											
												
												if tabla!=None:

													self.registro.append("db('"+tabla+"').relacionar("+str(i)+",'"+campo1+"',"+c+")")
													#nuevo
													#self.campos[self.seleccion][self.obtenerCampos(args["tabla"]).index(args["campo"])][1]=self.object
													self.consola("La relación fue efectuada con exito\n",self)
													
													self.relaciones[self.seleccion]=[i,campo1,args["tabla"],args["id"],args["campo"]]
													self.relaciones[args["tabla"]]=[args["id"],args["campo"],self.seleccion,i,campo1]
													self.lrelaciones.append("db('"+tabla+"').relacionar("+str(i)+",'"+campo1+"',"+c+")")

													
											except Exception,e:
													print "Error relacionar en bloque tabla<br>"
													print e
													self.registro.append("db.relacionar("+str(i)+",'"+campo1+"',"+c+")")
													#nuevo
													#self.campos[self.seleccion][self.obtenerCampos(args["tabla"]).index(args["campo"])][1]=self.object
													self.consola("La relación fue efectuada con exito\n",self)
													self.relaciones[self.seleccion]=[i,campo1,args["tabla"],args["id"],args["campo"]]
													self.relaciones[args["tabla"]]=[args["id"],args["campo"],self.seleccion,i,campo1]
													self.lrelaciones.append("db.relacionar("+str(i)+",'"+campo1+"',"+c+")")
													


									except Exception,e:
										print "Error en relacionar en bloque campo<br>"
										print e.args
										
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
												#nuevo
												self.relaciones[args["tabla"]]=[args["id"],args["campo"],self.seleccion,i,campo1]
									except:
											self.registro.append("db.relacionar("+str(i)+",'"+campo1+"',"+c+")")
											self.relaciones[self.seleccion]=[i,campo1,args["tabla"],args["id"],args["campo"]]
											#nuevo
											self.relaciones[args["tabla"]]=[args["id"],args["campo"],self.seleccion,i,campo1]

											self.consola("La relación fue efectuada con exito\n",self)
							return self
						else:
							print "El campo ",args["campo"]," a relacionar no existe en la tabla ",args["tabla"]
					except Exception,e:
						print "Error en relacionar "
						print e					
                  
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
			    self.long=long
			    self.all="<type 'all'>"
			    self.password="<type 'password'>"
			    self.email="<type 'email'>"
			    self.time="<type 'time'>"
			    self.date="<type 'date'>"
			    self.datetime="<type 'datetime'>"
			    self.url="<type 'url'>"
			    self.file="<type 'file'>"
			    self.bin="<type 'binary'>"
			    self.doc="<type 'doc'>"
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
			    
			    self.limite=1
			    

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
			db.registro=["# -*- coding: utf-8 -*-","try:\n from ztec.zdb import DB\nexcept:\n from zdb import DB","db=DB()"]
			db.rcampos=["# -*- coding: utf-8 -*-","try:\n from ztec.zdb import DB\nexcept:\n from zdb import DB","db=DB()"]

			
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
						

	
