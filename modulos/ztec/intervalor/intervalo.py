#!/usr/bin/python
#-*- codign:utf-8 -*-

def mostrarConjuntos(cadena,conjuntos):
	l=[]
	for elem in conjuntos:
		l.append(cadena[elem[0]:elem[1]])
	return l

def getConjuntos(cadena,etiquetas,exclusion=None):
	aperturas=[]
	cierres=[]
	c=0
	activa=False
	conjuntos=[]
	ex_aper=[]
	ex_cier=[]
	exclusiones=[]
	while c+len(etiquetas[1])<=len(cadena):
		if exclusion!=None:
			if type(exclusion)==list:
				if cadena[c:c+len(exclusion[0])]==exclusion[0]:
					activa=True
					ex_aper.append(c)
				
				if cadena[c:c+len(exclusion[1])]==exclusion[1]:
					activa=False
					c+=len(exclusion[1])
					ex_cier.append(c)
			else:
				c+=len(exclusion)	
		
		if activa==False:
			if cadena[c:c+len(etiquetas[0])]==etiquetas[0]:
				aperturas.append(c)
			if cadena[c:c+len(etiquetas[1])]==etiquetas[1]:
				cierres.append(c)
		c+=1
	
	c=0
	for elem in aperturas:
		conjuntos.append([elem,cierres[c]])
		c+=1
	c=0
	for elem in ex_aper:
		exclusiones.append([elem,ex_cier[c]])
		c+=1
	return [conjuntos,exclusiones]
	


	
def unir(c1,c2):
	if c1[0]>=c2[0]:
		c3=[c1[0]]
	else:
		c3=[c2[0]]
	if c1[1]>=c2[1]:
		c3.append(c1[1])
	else:
		c3.append(c2[1])
	return c3	
def inter(c1,c2):
	if c1!=[]:
		if c2!=[]:
			if c1[0]>=c2[0]:
				c3=[c1[0]]
			else:
				c3=[c2[0]]
			if c1[1]>=c2[1]:
				c3.append(c2[1])
			else:
				c3.append(c1[1])
			if c3[0]>c3[1]:
				return []
			else:
				return c3
		else:
			return c1
	else:
		return[]
	
def interAll(c1,*cs):
	for elem in cs:
		c1=inter(c1,elem)
	return c1
def interList(c1,cs):
	for elem in cs[0]:
		c1=inter(c1,elem)
	return c1
def interInv(c1,c2):
	if c1[0]<=c2[0]:
		c3=[c1[0],c2[0]]
	else:
		c3=[c2[0],c1[0]]

	if c1[1]>=c2[1]:
		c4=[c2[1],c1[1]]
	else:
		c4=[c1[1],c2[1]]
	return [c3,c4]


def interInvAll(c)

