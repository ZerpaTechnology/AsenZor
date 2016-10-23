#!/usr/bin/python
#-*- codign:utf-8 -*-

import intervalo as i
f=open("test.html","r")
t=f.read()
f.close()

conjuntos,exclusiones=i.getConjuntos(t,["<div>","</div>"],["{{","}}"])
#"hola mundo"
# 0123456789
e=[[17, 40], [41, 65]]
con=[0,len(t)]
#print "=========================="
#print "conjuntos: ",conjuntos
#print i.mostrarConjuntos(t,conjuntos)
#print "---------------------------"
#print "exclusiones: ",exclusiones
#print i.mostrarConjuntos(t,exclusiones)
l=[]
for html in conjuntos:
	l.append("print '"+t[html[0]:html[1]]+"'")
	for python in exclusiones:
		if html[1]<python[0]:
			l.append(t[python[0]:python[1]][2:-2])
	

print l 

