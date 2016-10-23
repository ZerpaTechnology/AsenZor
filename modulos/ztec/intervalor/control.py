#!/usr/bin/python
#-*- codign:utf-8 -*-

import intervalo as i
f=open("test.html","r")
t=f.read()
f.close()

#conjuntos,exclusiones=i.getConjuntos(t,["<div>","</div>"],["{{","}}"])
#"hola mundo"
# 0123456789
#print conjuntos
#print "conjuntos: ",conjuntos
#print i.mostrarConjuntos(t,conjuntos)
#print "---------------------------"
#print "exclusiones: ",exclusiones
#print i.mostrarConjuntos(t,exclusiones)
#print ""
#print "============================="
#c=i.interInvAll(i.getInterval(t),exclusiones)
#c=i.interInv([0,4],[4,10])
#print c
#print ""
#print "#############################"
#print i.mostrarConjuntos("hola mundo",c)
#print i.unir([40,50],[20,30])
#print i.seJunta([5,40],[20,30])

print i.unirAll([5,500],[[100,150],[200,250],[300,310],[340,350]])