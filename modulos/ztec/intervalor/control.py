#!/usr/bin/python
#-*- codign:utf-8 -*-
import sys
sys.path.append("../")
import os
def convertir(t):
	import intervalo as i
	import sys
	
	import ztec.zu as zu
	

	cpython=True
	ultimo=0
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
	if "{{" in t and "}}":
		if type(HTML[0])==list:

			for html in HTML:
				codhtml="print '"+t[html[0]:html[1]].replace("\n","")+"'"+"\n"
				if codhtml!="print ''\n":
					l.append(iden+codhtml)
				for python in PYTHON:
					print html[1], " | ", python[0]
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
						lpass=len("return ")
						lreturn=len("pass ")
						l.append(iden+codpython)

						if tab=="":

							if codpython[0:lfor]=="for ":
								iden+="  "
							if codpython[0:lwhile]=="while ":
								iden+="  "
							if codpython[0:lif]=="if ":
								iden+="  "
							if codpython[0:lelse]=="else: ":
								iden+="  "
							if codpython[0:ltry]=="try:":
								iden+="  "
							if codpython[0:lexcept]=="except ":
								iden+="  "
							if codpython[0:lelif]=="elif ":
								iden+="  "
							if codpython[0:lpass]=="pass\n":
								iden=iden[:-2]
							if codpython[0:lreturn]=="return ":
								iden=iden[:-2]
						else:

							liden=len(iden)
							
							if codpython[liden:liden+lfor]=="for ":
								iden+="  "
							if codpython[liden:liden+lwhile]=="while ":
								iden+="  "
							if codpython[liden:liden+lif]=="if ":
								iden+="  "
							if codpython[liden:liden+lelse]=="else: ":
								iden+="  "
							if codpython[liden:liden+ltry]=="try:":
								iden+="  "
							if codpython[liden:liden+lexcept]=="except ":
								iden+="  "
							if codpython[liden:liden+lelif]=="elif ":
								iden+="  "
							if codpython[:lpass]=="pass\n":
								iden=iden[:-2]
							
							if codpython[liden:lreturn]=="return ":
								iden=iden[:-2]					

						
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
