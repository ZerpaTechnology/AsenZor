#!/usr/bin/python
#-*- codign:utf-8 -*-

def mostrarConjuntos(cadena,conjuntos):
	l=[]
	for elem in conjuntos:
		l.append(cadena[elem[0]:elem[1]])
	return l

def getU(c1,c2):
	if type(c1[0])==list or type(c1[0])==tuple:
		if type(c2[0])==list or type(c2[0])==tuple:
			if c1[0][0]>=c2[0][0]:
				c3=[c1[0][0]]
			else:
				c3=[c2[0][0]]
			if c1[-1][1]>=c2[-1][1]:
				c3.append(c1[-1][1])
			else:
				c3.append(c2[-1][1])
			return c3
		else:
			if c1[0][0]>=c2[0]:
				c3=[c2[0]]
			else:
				c3=[c1[0][0]]
			if c1[-1][1]>=c2[1]:
				c3.append(c1[-1][1])
			else:
				c3.append(c2[1])
		return c3
	else:

		if type(c2[0])==list or type(c2[0])==tuple:
			if c1[0]>=c2[0][0]:
				c3=[c1[0]]
			else:
				c3=[c2[0][0]]
			if c1[-1]>=c2[-1][1]:
				c3.append(c1[-1][1])
			else:
				c3.append(c2[-1][1])
			return c3
		else:

			if c1[0]>=c2[0]:
				c3=[c2[0]]

			else:
				c3=[c1[0]]
			if c1[1]>=c2[1]:
				c3.append(c1[1])
			else:
				c3.append(c2[1])
			return c3

						


def getConjuntos(cadena,etiquetas,exclusion=None):
	aperturas=[]
	cierres=[]
	c=0
	activa=False
	conjuntos=[]
	ex_aper=[]
	ex_cier=[]
	exclusiones=[]
	while c+len(etiquetas[1])<len(cadena):
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
				aperturas=[c]
			if cadena[c:c+len(etiquetas[1])]==etiquetas[1]:
				cierres=[c]
		c+=1
	
	
	c=0
	for elem in ex_aper:
		exclusiones.append([elem,ex_cier[c]])
		c+=1
	conjuntos=interInvAll([0,len(cadena)],exclusiones)
	return [conjuntos,exclusiones]
	
def seJunta(c1,c2):
	i1=c1[0]
	i2=c2[0]
	f1=c1[1]
	f2=c2[1]
	if i1<=i2 and f1<=f2 and f1>=i2:
		return True
	elif i2<=i1 and  i1<f1 and f2>=i1 and f2<=f1:
		return True
	else:
		#seccion nueva
		if i2<=i1 and f2>=f1 or i2>=i1 and f2<=f1:
			return True
		else:
			return False

#al parecer esta listo
# c1 es un intervalo y c2 es una lista de intervalos
def unirAll(c1,c2):
	c=0
	l=[c1]

	while c<len(c2):
		if seJunta(c1,c2[c])==True:
			l.extend([unir(l[-1],c2[c])])
			del l[-2]
			
		else:
			
			if len(l)==1:
				
				l=unir(l[-1],c2[c])
			else:
				l.extend(unir(l[-1],c2[c]))
				del l[-3]
		
		c+=1
	return l

def unir(c1,c2):
	if type(c1[0])==list or type(c1[0])==tuple:
		if type(c2[0])==list or type(c2[0])==tuple:
			pass
		else:
			#si c1 es una lista y c2 no lo es
			print "funcion no soportada haga paso a paso la union con unirAll"

	else:
		if type(c2[0])==list or type(c2[0])==tuple:
			print "funcion no soportada haga paso a paso la union con unirAll"

		else:
			#seccion lista
			i1=c1[0]
			i2=c2[0]
			f1=c1[1]
			f2=c2[1]
			#listo
			#1
			
			
			if i1<=i2 and f1<=f2 and f1>=i2:
				if i1<=i2 and f1<=f2:
					
					c3=[i1]
				else:
					c3=[i2]

				if f1>=f2 and i1>=i2:
					c3.append(f1)
				else:
					c3.append(f2)
				return c3
			#listo
			#2
			elif i2<=i1 and  i1<f1 and f2>=i1 and f2<=f1:
				
				return [i2,f1]


			else:
				if i2<=i1 and f2>=f1 or i2>=i1 and f2<=f1:
					#uno contien a otro
					if i1<=i2 and f1>=f2:
						return [i1,f1]
					else:
						return [i2,f2]
				else:
					#no se juntan
					if i1>=i1 and f1>=f2:
						return [c2,c1]
					else:
						return [c1,c2]



#captura c1 en c2

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
#[cerrado,abierto]
#borra c2 en c1
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


def interInvAll(c1,cs):
	for elem in cs:
		
		c1=interInv(c1,elem)
		
	return c1

def getInterval(string):
	return[0,len(string)-1]