#!/usr/bin/python
#-*- codign:utf-8 -*-

import intervalo as i
f=open("test.html","r")
t=f.read()
f.close()

conjuntos,exclusiones=i.getConjuntos(t,["<div>","</div>"],["{{","}}"])

print conjuntos
print exclusiones
c=i.unir(conjuntos[0],conjuntos[1])
#print c
c=i.interInv(c,exclusiones[0])
#print c
print i.mostrarConjuntos(t,c)