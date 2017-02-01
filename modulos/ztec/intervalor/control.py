#!/usr/bin/python
#-*- codign:utf-8 -*-
#python {{}}
#php <?php ?>
#ruby <% %>
#java <$ $>


import sys
sys.path.append("../")
import os
#para identacion
def convertir(t):
	import intervalo as i
	import sys
	
	import ztec.zu as zu
	
	cpython=True
	ultimo=0
	#nota si dice list index out range estar pendiente que el embebido este dentro de
	#etiquestas por ejemplo <div></<div>
	PYTHON,ex=i.getConjuntos(t,["{{","}}"])


	HTML=i.borrarAll([0,len(t)],PYTHON)

	#"hola mundo"
	# 0123456789
	
	e=[[17, 40], [41, 65]]
	con=[0,len(t)]
	#print "=========================="
	#print "conjuntos: ",conjuntos
	#print i.mostrarConjuntos(t,[conjuntos])
	#print "---------------------------"
	#print "exclusiones: ",exclusiones
	#print i.mostrarConjuntos(t,exclusiones)
	l=[]
	#print "HTML ", HTML
	#print "python ",PYTHON
	iden=""
	
	if "{{" in t and "}}" in t:

		if type(HTML[0])==list:

			for html in HTML:
				codhtml="print '''"+t[html[0]:html[1]].replace("\n","")+"'''"+"\n"
				if codhtml!="print ''\n":
					l.append(iden+codhtml)
				for python in PYTHON:
					
					if html[1]==python[0]:
						
						codpython=t[python[0]:python[1]][2:-2]+"\n"
						tab=zu.getTab(codpython)
						lfor=len("for ")
						lwhile=len("while ")
						lif=len("if ")
						lelse=len("else:")
						ltry=len("try:")
						lexcept=len("except ")
						lelif=len("elif ")
						lpass=len("pass")
						lreturn=len("return ")
						
						if tab=="":
							
							if codpython[0:lfor]=="for ":
								l.append(iden+codpython)
								iden+="  "
							elif codpython[0:lwhile]=="while ":
								
								l.append(iden+codpython)
								iden+="  "
							elif codpython[0:lif]=="if ":
								
								l.append(iden+codpython)
								iden+="  "
							elif "else:" in codpython[0:lelse]:
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif "try:" in codpython[0:ltry]:
								
								l.append(iden+codpython)
								iden+="  "
							elif "except" in codpython[0:lexcept]:
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif codpython[0:lelif]=="elif ":
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif codpython[0:lpass]=="pass" and codpython=="pass\n":
								l.append(iden+codpython)
								iden=iden[:-2]
							elif codpython[0:lreturn]=="return ":
								l.append(iden+codpython)
								iden=iden[:-2]
							else:
								l.append(iden+codpython)

						else:

							liden=len(iden)
							
							if codpython[liden:liden+lfor]=="for ":
								l.append(iden+codpython)
								iden+="  "
							elif codpython[liden:liden+lwhile]=="while ":
								l.append(iden+codpython)
								iden+="  "
							elif codpython[liden:liden+lif]=="if ":
								l.append(iden+codpython)
								iden+="  "

							elif "else:" in codpython[liden-2:liden+lelse]:
								
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif "try:" in codpython[liden:liden+ltry]:
								l.append(iden+codpython)
								iden+="  "
							elif "except" in codpython[liden-2:liden+lexcept]:
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif codpython[liden-2:liden+lelif]=="elif ":
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif codpython[:lpass]=="pass" and codpython=="pass\n":
								l.append(iden+codpython)
								iden=iden[:-2]
							
							elif codpython[liden:lreturn]=="return ":
								l.append(iden+codpython)
								iden=iden[:-2]	
							else:
								l.append(iden+codpython)

						

						
		else:
			l.append(t[HTML[0]:HTML[1]])
		txt=""
		for elem in l:
			txt+=elem
		return txt
	else:

		return 'print """'+t+'"""'

def generar(rutahtml,rutapython,cabecera=""):
	#vista html
	(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(rutahtml)
	#vista python
	if os.path.exists(rutapython):


		(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = os.stat(rutapython)
		if mtime!=mtime2:
			f=open(rutahtml,"r")
			t=f.read()

			f.close()

			f=open(rutahtml,"w")

			
			f.write(t)
			f.close()
			txt=convertir(t)
			f=open(rutapython,"w")
			f.write(cabecera+txt)
			f.close()
			return True
	else:

			f=open(rutahtml,"r")
			t=f.read()
			f.close()
			
			f=open(rutahtml,"w")
			f.write(t)
			f.close()
			
			txt=convertir(t)

			f=open(rutapython,"w")
			f.write(cabecera+txt)
			f.close()	
			return True
	return False	



#para no indentacion
def convertir2(t,etiquetas=["{{","}}"]):
	import intervalo as i
	import sys
	
	import ztec.zu as zu
	
	cpython=True
	ultimo=0
	PYTHON,ex=i.getConjuntos(t,etiquetas)


	HTML=i.borrarAll([0,len(t)],PYTHON)

	#"hola mundo"
	# 0123456789
	e=[[17, 40], [41, 65]]
	con=[0,len(t)]
	#print "=========================="
	#print "conjuntos: ",conjuntos
	#print i.mostrarConjuntos(t,[conjuntos])
	#print "---------------------------"
	#print "exclusiones: ",exclusiones
	#print i.mostrarConjuntos(t,exclusiones)
	l=[]
	#print "HTML ", HTML
	#print "python ",PYTHON
	iden=""
	inicial=True#si es la primera linea
	first=False #si hay un print en el html y no hay continuacion previa
	primero=False#si si hay un print en el python y hay continuacion
	
	

	if etiquetas[0] in t and etiquetas[1] in t:

		if type(HTML[0])==list:

			for html in HTML:
				if inicial==True:
					if first==False:
						if t[html[0]:html[1]][0]=="'" or t[html[0]:html[1]][-1]=="'":
							codhtml='print """'+t[html[0]:html[1]].replace("\n","")+'"""'
						elif t[html[0]:html[1]][0]=='"' or t[html[0]:html[1]][-1]=='"':
							codhtml="print '''"+t[html[0]:html[1]].replace("\n","")+"'''"
						else:
							codhtml="print '''"+t[html[0]:html[1]].replace("\n","")+"'''"
						inicial=False
						first=True
						primero
					else:
						if t[html[0]:html[1]][0]=="'" or t[html[0]:html[1]][-1]=="'":
							codhtml='+"""'+t[html[0]:html[1]].replace("\n","")+'"""'
						elif t[html[0]:html[1]][0]=='"' or t[html[0]:html[1]][-1]=='"':
							codhtml="+'''"+t[html[0]:html[1]].replace("\n","")+"'''"
						else:
							codhtml="+'''"+t[html[0]:html[1]].replace("\n","")+"'''"
						
				else:
					
					if first==False:

						if t[html[0]:html[1]][-1]=="'" or t[html[0]:html[1]][0]=="'":
							
							codhtml='print """'+t[html[0]:html[1]].replace("\n","")+'"""'
						elif t[html[0]:html[1]][-1]=='"' or t[html[0]:html[1]][0]=='"':
							codhtml="print '''"+t[html[0]:html[1]].replace("\n","")+"'''"
						else:
							codhtml="print '''"+t[html[0]:html[1]].replace("\n","")+"'''"
						first=True
						primero=True
						
					else:
						
						if t[html[0]:html[1]][-1]=='"' or t[html[0]:html[1]][0]=='"':
							codhtml="+'''"+t[html[0]:html[1]].replace("\n","")+"'''"
						elif t[html[0]:html[1]][-1]=="'" or t[html[0]:html[1]][0]=="'":
							codhtml='+"""'+t[html[0]:html[1]].replace("\n","")+'"""'
						else:
							codhtml="+'''"+t[html[0]:html[1]].replace("\n","")+"'''"




				if codhtml!="''\n":
					l.append(iden+codhtml)
				for python in PYTHON:
					
					if html[1]==python[0]:
						codpython=t[python[0]:python[1]][2:-2]
						tab=zu.getTab(codpython)
						lfor=len("for ")
						lwhile=len("while ")
						lif=len("if ")
						lelse=len("else")
						ltry=len("try:")
						lexcept=len("except ")
						lelif=len("elif ")
						lpass=len("pass")
						lreturn=len("return ")
						lprint=len("print ")
						
						if tab=="":
							

							if codpython[0:lfor]=="for ":

								if ":" in codpython[lfor:]:
									l.append("\n"+iden+codpython+"\n")
									iden+="  "
								else:
									l.append(iden+codpython)
								first=False
								primero=False
							elif codpython[0:lwhile]=="while ":
								
								l.append("\n"+iden+codpython)
								iden+="  "
								first=False
								primero=False
							elif "print " in codpython[0:lprint]:
								
								if first==False:
									l.append(iden+codpython)				
								else:
									if primero==True:
										l.append(iden+"+str("+codpython[lprint:]+")")
									else:
										l.append(iden+"+str("+codpython[lprint:]+")")
										#estar pendiente de este primero ya que se hizo un cambio en la condicion
										primero=True
				
							elif codpython[0:lif]=="if ":

								if ":" in codpython[lif:]:

								
									l.append("\n"+iden+codpython+"\n")
									iden+="  "
								else:
									l.append(iden+codpython)
								first=False
								primero=False
								

							elif "else" in codpython[0:lelse]:
								first=False
								primero=False
								
								if ":" in codpython[lelse:]:
									iden=iden[:-2]
									l.append("\n"+iden+codpython+"\n")
									iden+="  "
								else:
									l.append(iden+codpython)
								

							elif "try:" in codpython[0:ltry]:
								
								l.append("\n"+iden+codpython)
								iden+="  "
								first=False
								primero=False
							elif "except" in codpython[0:lexcept]:
								iden=iden[:-2]
								l.append("\n"+iden+codpython)
								iden+="  "
								first=False
								primero=False
							elif codpython[0:lelif]=="elif ":
								iden=iden[:-2]
								
								l.append("\n"+iden+codpython)
								iden+="  "
								first=False
								primero=False
							elif codpython[0:lpass]=="pass" and len(codpython)==lpass:
								l.append("\n"+iden+codpython+"\n")
								iden=iden[:-2]
								first=False
								primero=False
							elif codpython[0:lreturn]=="return ":
								l.append("\n"+iden+codpython)
								iden=iden[:-2]
								first=False
								primero=False

							else:
								first=False
								primero=False

								l.append("\n"+iden+codpython+"\n")

						else:
							

							liden=len(iden)
							
							
							if codpython[liden:liden+lfor]=="for ":
								
								first=False
								primero=False
								if ":" in codpython[liden+lfor:]:
									l.append("\n"+iden+codpython+"\n")
									iden+="  "
								else:
									l.append(iden+codpython)

							elif codpython[liden:liden+lwhile]=="while ":
								first=False
								primero=False
								if ":" in codpython[liden+lwhile:]:
									l.append("\n"+iden+codpython)
									iden+="  "
								else:
									l.append(iden+codpython)

							elif codpython[liden:liden+lif]=="if ":
								first=False
								primero=False
								if ":" in codpython[liden+lif:]:
									l.append("\n"+iden+codpython)
									iden+="  "
								else:
									l.append(iden+codpython)



							elif "else" in codpython[liden-2:liden+lelse]:
								
								if ":" in codpython[liden+lelse:]:
									iden=iden[:-2]
									l.append("\n"+iden+codpython)
									iden+="  "
								else:
									l.append(iden+codpython)
								first=False
								primero=False

							elif "try:" in codpython[liden:liden+ltry]:
								l.append("\n"+iden+codpython)
								iden+="  "
								first=False
								primero=False
							elif "except" in codpython[liden-2:liden+lexcept]:
								iden=iden[:-2]
								l.append("\n"+iden+codpython)
								iden+="  "
								first=False
								primero=False
							elif codpython[liden-2:liden+lelif]=="elif ":
								iden=iden[:-2]
								l.append("\n"+iden+codpython)
								iden+="  "
								first=False
								primero=False
							elif codpython[:lpass]=="pass" and len(codpython)==lpass:
								l.append("\n"+iden+codpython+"\n")
								iden=iden[:-2]
								first=False
								primero=False
							
							elif codpython[liden:lreturn]=="return ":
								l.append("\n"+iden+codpython)
								iden=iden[:-2]
								first=False
								primero=False
							elif codpython[:lprint]=="print ":
								if first==False:
									l.append(iden+codpython)				
								else:
									if primero==True:
										l.append(iden+"+str("+codpython[lprint:]+")")
									else:
										l.append(iden+"+str("+codpython+")")

							else:

								l.append("\n"+iden+codpython)
								first=False
								primero=False
					

						
					
			

		else:
			l.append(t[HTML[0]:HTML[1]])
		txt=""
		for elem in l:
			txt+=elem
		return txt
	else:

		return 'print """'+t+'"""'

def generar2(rutahtml,rutapython,cabecera=""):
	#vista html
	(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(rutahtml)
	#vista python
	if os.path.exists(rutapython):
		(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = os.stat(rutapython)
		if mtime!=mtime2:
			f=open(rutahtml,"r")
			t=f.read()

			f.close()

			f=open(rutahtml,"w")

			
			f.write(t)
			f.close()
			txt=convertir2(t)
			f=open(rutapython,"w")
			f.write(cabecera+txt)
			f.close()
			return True
	else:
			f=open(rutahtml,"r")
			t=f.read()
			f.close()
			
			f=open(rutahtml,"w")
			f.write(t)
			f.close()
		
			txt=convertir2(t)
			f=open(rutapython,"w")
			f.write(cabecera+txt)
			f.close()	
			return True
	return False	
