#!/usr/bin/python
#-*- codign:utf-8 -*-

import intervalo as i
f=open("test.html","r")
t=f.read()
f.close()

conjuntos,exclusiones=i.getConjuntos(t,["<div>","</div>"],["{{","}}"])

print "conjuntos: ",conjuntos
print i.mostrarConjuntos(t,conjuntos)
print "---------------------------"
print "exclusiones: ",exclusiones


print i.mostrarConjuntos(t,exclusiones)

