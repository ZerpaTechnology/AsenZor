#!/usr/bin/python
#-*- codign:utf-8 -*-

def mostrarConjuntos(cadena,conjuntos):
	l=[]
	for elem in conjuntos:
		l.append(cadena[elem[0]:elem[1]])
	return l
#al parecer esta completa
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
		else:
			pass
		if activa==False:
			if cadena[c:c+len(etiquetas[0])]==etiquetas[0]:
				
				aperturas.append(c)
			if cadena[c:c+len(etiquetas[1])]==etiquetas[1]:
				
				cierres.append(c+len(etiquetas[1]))
		c+=1
	
	
	
	c=0
	for elem in aperturas:
		conjuntos.append([elem,cierres[c]])
		c+=1
	if exclusion==None:
		exclusiones=None
		
	else:
		c=0
		for elem in ex_aper:
			exclusiones.append([elem,ex_cier[c]])
			c+=1
		conjuntos=borrar([aperturas[0],cierres[0]],exclusiones)

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
#no lista trabajar con funciones invertidas
def unirInv(c1,c2):
	print "unirInv ",getU(c1,c2)
	return interAll(getU(c1,c2),unir(c1,c2))

#al parecer esta completa
def unir(c1,c2):
	if type(c1[0])==list or type(c1[0])==tuple:
		if type(c2[0])==list or type(c2[0])==tuple:
			
			c1[0]=unirAll(c1[0],c2)
			
			if len(c1[0])>1:
				c=1
				while c<len(c1):
					
					c1[0]=unirAll(c1[c],c1[0])
					c+=1
			return c1[0]
		else:
			#si c1 es una lista y c2 no lo es
			#print "funcion no soportada haga paso a paso la union con unirAll"

			return unirAll(c2,c1)

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


#al parecer esta listo
#captura c1 en c2
def inter(c1,c2,unicos=True):
	l=[]
	if c1!=[]:
		if c2!=[]:
			if type(c1[0])==list or type(c1[0])==tuple:
				if type(c2[0])==list or type(c2[0])==tuple:
				
					if unicos==True:
						
						con1=0
						while con1<len(c1):
							con2=0
							while con2<len(c2):
								l.append(inter(c1[con1],c2[con2]))
								con2+=1
							con1+=1
						return l
								
					else:
						con1=1
						c1[0]=inter(c1[0],c2[0],unicos)
					
						while con1<len(c1):
							con2=0
							while con2<len(c2):
								c1[0]=inter(c1[0],c2[con2],unicos)
								con2+=1
							c1[0]=inter(c1[0],c1[con1],unicos)
							con1+=1
						return c1[0]

				else:
					print type(c1[0])
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
			if unicos==True:
				return l
			else:
				return c1
	else:
		return[]
#listo
#True devuelve intervalos de interseccion
#False devuelve el conjunto que interseccta a todos
def interAll(c1,cs,unicos=True):
	l=[]
	for elem in cs:
		if unicos==True:
			if seJunta(c1,elem):
				c2=inter(c1,elem)
				if c2!=[]:
					l.append(c2)
		else:
			c1=inter(c1,elem)
	if unicos==True:
		return l
	else:
		return c1


def interList(c1,cs):
	for elem in cs[0]:
		c1=inter(c1,elem)
	return c1
#[cerrado,abierto]
#retorna los intervalos no se intersectan entre c1 y c2
def interInv(c1,c2):
		if type(c1[0])==list or type(c1[0])==tuple:
			if type(c2[0])==list or type(c2[0])==tuple:
				con1=0
				while con1<len(c1):
					con2=0
					while con2<len(c2):
						if seJunta(c1[con1],c2[con2]):
							c1[con1]=interInv(c1[con1],c2[con2])
						con2+=1

					con1+=1
				return c1
			else:
				print "sdwsds"
				con1=0
				l=[]
				while con1<len(c1):
					print "c1[con1] ",c1[con1]," c2: ",c2
					if seJunta(c1[con1],c2):
						print "sii"
						l.extend(interInv(c1[con1],c2))
					con1+=1
				return l
		
		else:
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
#listo
#se parece mucho al interInv
#borra c2 en c1
def borrar(c1,c2):
	
	if type(c1[0])==list or type(c1[0])==tuple:
			if type(c2[0])==list or type(c2[0])==tuple:

				con1=0
				while con1<len(c1):
					con2=0
					while con2<len(c2):
						c1[con1]=borrar(c1[con1],c2[con2])
						con2+=1
					con1+=1
				l=[]
				for elem in c1:
					if type(elem[0])==list:
						l.extend(elem)
					else:
						l.append(elem)
				return l

			else:
				#al parecer listo
				c=0
				while c<len(c1):
					c1[c]=borrar(c1[c],c2)
					c+=1
				l=[]
				for elem in c1:
					if type(elem[0])==list:
						l.extend(elem)
					else:
						l.append(elem)
				return l		
	else:
		if type(c2[0])==list or type(c2[0])==tuple:
			return borrarAll(c1,c2)
		else:
			if seJunta(c1,c2):
				i1=c1[0]
				f1=c1[1]
				i2=c2[0]
				f2=c2[1]
				if i1!=i2 and f1==f2 or i1==i2 and f1!=f2 or i1!=i2 and f1!=f2: 
					
					if i1>=i2 and f1>=f2:

						return [f2,f1]
					elif i1<=i2 and f1<=f2:

						return [i1,i2]
					elif i1<i2 and f1>f2:
						return [[i1,i2],[f2,f1]]
					else:
						return []
				else:
					
					return []
			else:
				
				return c1

#al parecer esta listo
def borrarAll(c1,c2):
	c=0
	
	for elem in c2:
		
		c1=borrar(c1,elem)	
		
		c+=1
	
	return c1