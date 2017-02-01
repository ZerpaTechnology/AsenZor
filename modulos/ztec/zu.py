#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
#18-1-2015
import math
import random

try:
	import pygame
	activo=True
except:
	activo=False

def invertString(cad):
	c=""
	for elem in cad:
		c=elem+c
	return c
def DateTime(H=0,M=0,S=0,d=0,w=0,mS=0,fechaHora=None,plus="+",formato='%d/%m/%y %H:%M:%S',num=None,obj=False,ignorar=[]):
	from datetime import datetime, date, time, timedelta
	import calendar
	for elem in ignorar:
		formato=formato.replace(elem,"")
	if fechaHora!=None:
		ahora=fechaHora
	else:
		ahora=datetime.now()
	if plus=="+":
		ahora+=timedelta(hours=H,minutes=M,seconds=S,days=d,weeks=w,microseconds=mS)
	elif plus=="-":
		ahora-=timedelta(hours=H,minutes=M,seconds=S,days=d,weeks=w,microseconds=mS)
	else:
		print "Solo esta permitido sumar o restar."
	if num=="dia":
		return ahora.day
	elif num=="mes":
		return ahora.month
	elif num=="año":
		return ahora.year
	elif num=="hora":
		return ahora.hours
	elif num=="minuto":
		return ahora.minute
	elif num=="segundo":
		return ahora.second
	else:
		if obj==False:
			return formato.replace("%d",str(ahora.day)).replace("%m",str(ahora.month)).replace("%y",str(ahora.year)).replace("%H",str(ahora.hour)).replace("%M",str(ahora.minute)).replace("%S",str(ahora.second))
		else:
			return ahora



"""
def sumarDateTime(datetime,H=None,M=None,S=None,d=None,m=None,y=None,viciesto=False):
	if " - " in datetime:
		_time,date=datetime.split(" - ")
		if "/" in date:
			_d,_m,_y=date.split("/")
			_d=int(_d)
			_m=int(_m)
			_y=int(_y)

		if ":" in _time:
			_H,_M,_S=_time.split(":")
			print "aaaaaaaaaaa"
			if S!=None:
				if S+int(_S)>59:
					minutosFloat=str(float(S+int(_S))/60)
					minutosStr,_S=minutosFloat.split(".")
					_S=str(float("0."+_S)*60).split(".")[0]
					if M!=None:

						if M+int(_M)+int(minutosStr)>59:
							_M=str(int(minutosStr)+int(M)+int(_M))
							horasFloat=str(float(_H)/60)
							horasStr,_M=minutosFloat.split(".")
							_M=str(int(float("0."+_M)*60)).split(".")[0]

							if H!=None:
								if int(horasStr)+int(_H)>23:
									_H=str(float(horasStr)+float(_H)/24)
									dias,_H=_H.split(".")
									_H=str(int(float("0."+_H)*24)).split(".")[0]
									_d+=int(dias)
									if _m=="1" or _m=="3" or _m=="5" or _m=="7" or _m=="8" or _m=="10" or _m=="12":
										if _d>31:
											meses,_d=str(float(_d)/31).split(".")
											_d=str(float(_d)*31).split(".")[0]
											if int(meses)+_m>12:
												a,_d=str((float(meses)+_m)/12).split(".")
												_y=str(a+_y)

									elif _m=="2":#viciesto
										if viciesto==False:
											if _d>28:
												meses,_d=str(float(_d)/28).split(".")
												_d=str(float(_d)*28).split(".")[0]
												if int(meses)+_m>12:
													a,_d=str((float(meses)+_m)/12).split(".")
													_y=str(a+_y)
										else:
											if _d>29:
												meses,_d=str(int(_d)/29)
												_d=str(float(_d)*29).split(".")[0]
												if int(meses)+_m>12:
													a,_d=str((float(meses)+_m)/12).split(".")
													_y=str(a+_y)

									else:
										if _d>30:
											meses,_d=str(int(_d)/30)
											_d=str(float(_d)*29).split(".")[0]
											if int(meses)+_m>12:
												a,_d=str((float(meses)+_m)/12).split(".")
												_y=str(a+_y)

							else:
								pass

						else:
							#_M=str(int(minutosStr)+int(M)+int(_M))
							pass

					else:
						#_M=str(int(minutosStr)+int(_M))
						_M=int(minutosStr)+int(_M)
				else:
					_S=int(_S)+int(S)
			else:
				if M!=None:
						if M+int(_M)+int(minutosStr)>59:
							_M=str(int(minutosStr)+int(M)+int(_M))
							horasFloat=str(float(_H)/60)
							horasStr,_M=minutosFloat.split(".")
							_M=str(int(_M)*60)

							if H!=None:
								if int(horasStr)+int(_H)>23:
									_H=str(float(horasStr)+float(_H)/24)
									dias,_H=_H.split(".")
									_H=str(int(_H)*24)
									_d+=int(dias)
									if _m=="1" or _m=="3" or _m=="5" or _m=="7" or _m=="8" or _m=="10" or _m=="12":
										if _d>31:
											meses,_d=str(int(_d)/31)
											_d=_str(float(_d)*31)
											if int(meses)+_m>12:
												a,_d=str(float(meses)+_m/12).split(".")
												_y=str(a+_y)

									elif _m=="2":#viciesto
										if viciesto==False:
											if _d>28:
												meses,_d=str(int(_d)/28)
												_d=_str(float(_d)*28)
												if int(meses)+_m>12:
													a,_d=str(float(meses)+_m/12).split(".")
													_y=str(a+_y)
										else:
											if _d>29:
												meses,_d=str(int(_d)/29)
												_d=_str(float(_d)*29)
												if int(meses)+_m>12:
													a,_d=str(float(meses)+_m/12).split(".")
													_y=str(a+_y)

									else:
										if _d>30:
											meses,_d=str(int(_d)/30)
											_d=_str(float(_d)*30)
											if int(meses)+_m>12:
												a,_d=str(float(meses)+_m/12).split(".")
												_y=str(a+_y)
				else:
					if H!=None:
								if int(horasStr)+int(_H)>23:
									_H=str(float(horasStr)+float(_H)/24)
									dias,_H=_H.split(".")
									_H=str(int(_H)*24)
									_d+=int(dias)
									if _m=="1" or _m=="3" or _m=="5" or _m=="7" or _m=="8" or _m=="10" or _m=="12":
										if _d>31:
											meses,_d=str(int(_d)/31)
											_d=_str(float(_d)*31)
											if int(meses)+_m>12:
												a,_d=str(float(meses)+_m/12).split(".")
												_y=str(a+_y)

									elif _m=="2":#viciesto
										if viciesto==False:
											if _d>28:
												meses,_d=str(int(_d)/28)
												_d=_str(float(_d)*28)
												if int(meses)+_m>12:
													a,_d=str(float(meses)+_m/12).split(".")
													_y=str(a+_y)
										else:
											if _d>29:
												meses,_d=str(int(_d)/29)
												_d=_str(float(_d)*29)
												if int(meses)+_m>12:
													a,_d=str(float(meses)+_m/12).split(".")
													_y=str(a+_y)

									else:
										if _d>30:
											meses,_d=str(int(_d)/30)
											_d=str(float(_d)*30)
											if int(meses)+_m>12:
												a,_d=str(float(meses)+_m/12).split(".")
												_y=str(a+_y)





		return str(_H)+":"+str(_M)+":"+str(_S)+" - "+str(_d)+"/"+str(_m)+"/"+str(_y)
	else:
		if "/" in datetime:
			pass
		elif ":" in datetime:
			pass
"""

def randomString(lon=8,alp=True,noalp=True,num=True):
	v_num="0123456789"
	v_alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	v_noalp=",.;:-!$%()=?¿|@#{[]}~><"
	if alp==True and noalp==True and num==True:
		v=v_num+v_alp+v_noalp
	elif alp==True and noalp==False and num==True:
		v=v_num+v_alp
	elif alp==False and noalp==True and num==True:
		v=v_num+v_noalp
	elif alp==True and noalp==True and num==False:
		v=v_alp+v_noalp
	elif alp==False and noalp==False and num==True:
		v=v_num
	elif alp==True and noalp==False and num==False:
		v=v_alp
	elif alp==False and noalp==True and num==False:
		v=v_noalp
	else:
		return None

	c=0
	token=""
	while c<lon:
		token+=v[random.randrange(0,len(v))]
		c+=1
	return token



def cmpString(cad1,cad2,orden="1a.",mayor=True):
	c="aáàäbcdeéèëfghiíìïjklmnñoóòöpqrstuúùüvwxyzçḉ" if (mayor==True) else invertString("aáàäbcdeéèëfghiíìïjklmnñoóòöpqrstuúùüvwxyzçḉ")
	c1=c+c.upper()
	c2="0123456789" if (mayor==True) else invertString("0123456789")
	c3=",;.·:_+-*/^%=&~@#|()[]{}¡!¿?<>«»ºª¬'‘´`¨“”€ł¶ŧ←↓→øþæßðđŋħł¢µΩŁ¢®Ŧ¥↑ıØÞÆ§ÐªŊĦŁ©" if (mayor==True) else invertString(",;.·:_+-*/^%=&~@#|()[]{}¡!¿?<>«»ºª¬'‘´`¨“”€ł¶ŧ←↓→øþæßðđŋħł¢µΩŁ¢®Ŧ¥↑ıØÞÆ§ÐªŊĦŁ©")
	rango=len(cad1) if(len(cad1)<=len(cad2))else len(cad2)
	if orden=="1a.":
		cadena=c2+c1+c3
	elif orden==".a1":
		cadena=c3+c1+c2
	elif orden=="1.a":
		cadena=c2+c3+c1
	elif orden=="a.1":
		cadena=c1+c3+c2
	elif orden=="a1.":
		cadena=c1+c2+c3
	elif orden==".1a":
		cadena=c3+c2+c1
	for x in range(rango):
			if cadena.find(cad1[x])>cadena.find(cad2[x]):
				return True
			elif cadena.find(cad1[x])<cadena.find(cad2[x]):
				return False
			
		
	return None

def ordenLargString(l,mayor=True,largo=True,orden="1a."):
	nl=[]
	c=0
	pos=0
	while c<len(l):
		
		cad=l[c]#elementos en lista

		c2=0
		pos=0
		while c2<=len(nl)-1:
					
				if largo==True:
					if len(nl[c2])>len(cad):
						pos+=1
					
				
					elif len(nl[c2])==len(cad):
					
						if not cmpString(nl[c2],cad,mayor=mayor,orden=orden):
							pos+=1
						else:
							pass
									
					
						
							
						
					
				
					
				else: 
					#listo
					if len(nl[c2])<len(cad):
						pos+=1
				
					
					elif len(nl[c2])==len(cad):
						
						if   cmpString(nl[c2],cad,mayor=mayor,orden=orden):
								pass
						else:
								pos+=1	
						
					
				c2+=1
		
		nl.insert(pos,cad)
		c+=1 
	return nl

def getTab(linea):
	"""
	obtine una cadena con la sangria de la cadena pasada

	ejemplo:
	>>>getTab("  hola mundo")
	"  "

	"""
	c=0
	cadena=""
	while c <len(linea):
		if linea[c]=="\t" or linea[c]=="\r" or linea[c]==" ":
			cadena+=linea[c] 
		else:
			return cadena

		c+=1
	return cadena

def siguienteNivel(codigo,funcion=None):
	cadena=""
	cadena2=""
	c=0
	tab=len(getTab(codigo[c]))

	while c<len(codigo):
		if len(getTab(codigo[c]))>tab:
			cadena+=codigo[c]+"\n"
		elif len(getTab(codigo[c]))==tab:
			cadena2+=codigo[c]+"\n"
		c+=1

	if funcion!=None:
		return funcion(cadena[:-1].split("\n"))+cadena2
	else:
		return cadena[:-1]+cadena2

def finIndex(cadena,busca):
	return cadena.index(busca)+len(busca)-1
def compilarLambda(codigo):
	"""
	transforma el codigo con funciones lambda de pythonZ a python normal
	#pythonZ
	función=lambda a,b:
		retorna a+b

	#python
	funcion=lambda a,b:zlambda(a=a,b=b,codigo="a=2\nb=5\nreturn a+b")



	"""
	#codigo=codigo.split("\n") asumimos que esta en lineas
	c=0
	abierto=False
	tabulacion=0
	cadena=""
	cadena2=""
	punteros=[]
	
	while c<len(codigo)-1:
		if "lambda " in codigo[c] and "=" in codigo[c] and ":" in codigo[c] and abierto==False:
			abierto=True
			cadena=siguienteNivel(codigo[c+1:],compilarLambda)
			f=finIndex(codigo[c],"lambda")+1
			parametros=codigo[c][f:codigo[c].index(":")]
			cparametros=""
			for elem in parametros.split(","):
				cparametros+=elem+"="+elem+","

			cadena2+=codigo[c]+"zlambda("+cparametros[:-1]+",__codigo__='''"+cadena[:-1]+"''')\n"
			c+=len(cadena.split("\n"))-1

		else:
			cadena2+=codigo[c]+"\n"
		c+=1
	return cadena2


			


	
	
	
def remplazarFueraString(cadena,viejo,nuevo):
	inicio=0
	fin=0
	abierto=False
	abridor=None
	while fin<len(cadena)-1:
		if cadena[fin]=="'" or cadena[fin]=='"':
			if abierto==False:
				abierto=True
				abridor=cadena[fin]
				cadena=cadena[:inicio]+cadena[inicio:fin].replace(viejo,nuevo)+cadena[fin:]
			
				#print viejo,nuevo
			else:
				if abridor==cadena[fin]:
					abierto=False
					abridor=None
					inicio=fin
			 
		fin+=1
	return cadena


def ordLargString(lista,creciente=True):
	_lista=lista
	lista2=[]
	valor=""
	valor2=""
	for elem in _lista:
		if lista2==[]:
			lista2.append(elem)
		else:
			for elem2 in lista2:
					if len(elem)>len(elem2):
						valor=elem2
			lista2.insert(lista2.index(elem),valor)

			

	return lista2
#["aaa","a","aa"]
#"aaa"
#valor="aaa"
#valor="a"




def dimensionar(lista):
	c=""
	for elem in lista:
		c+="["+str(elem)+"]"

	return c

def add(lista,numero): #para lista con  numeros como elementos
	l=len(lista)
	c=0
	while c < l:
		lista[c]=lista[c]+numero
		c+=1
		
def add2(lista,lista2): #para lista con tuplas como elementos
	l=len(lista)
	c=0
	while c < l:
		lista[c]=[lista[c][0]+lista2[0],lista[c][1]+lista2[1]]
		c+=1
		
def restar(lista,numero):
	l=len(lista)
	c=0
	while c < l:
		lista[c]=lista[c]-numero
		c+=1
		
		

	
def mayor(lista):
	i=0
	for elem in lista:
		if type(elem) == int: 
			if elem > i:
				i=elem
	return i
	
#para porcentajes
def ciento(valor1,valor2):
	return (valor1*valor2)/100
	
#para valores relativos
def ciento2(valor1,valor2):
	return (valor1*100)/valor2

def diferenciar(v1,v2):
	l=[]
	for elem in v1:
		for elem2 in v2:
			if elem != elem2:
				l.append(elem2)
	return l
	
		
def por(v1,v2,f=1):
	if f==1:#{"v1.1":"v2.1","v1.2":"v2.2"}
		c=0
		d={}
		for elem in v1:
			d[str(elem)]=v2[c]
			c+=1
		return d
	if f==2:
		cadena=""
		for elem in v1:
			cadena+=str(elem)+","
		cadena=cadena[0:-1]
		return cadena

def mayor_f(lista,f=1):
	lista2=[]
	a=0
	m=0
	d=0
	for elem in lista:
		lista2.append(elem.split("/"))
		print elem.split("/")
	for elem in lista2:
		if elem[0]>d:
			d=elem[0]
		if elem[1]>m:
			m=elem[1]
		if elem[2]>a:
			a=elem[2]
	if f==1:
		return [d,m,a]	
	if f==2:
		return str(d)+"/"+str(m)+"/"+str(a) 
	
def u(valor,f=1):
	if f==1:
		c=0
		for elem in valor:
			valor[c]=elem.decode("utf-8")
			c+=1
		return valor
	if f==2:
		c=0
		for elem in valor:
			valor[c][0]=elem[0].decode("utf-8")
			c+=1
		return valor	
def u2(valor):
	return str(valor).replace("\\xc3\\xb3","ó").replace("\\xc3\\xba","ú").replace("\\xc3\\xad","í").replace("\\xc2\\xa1","!").replace("\\xc3\\xb1","ñ")

def nu2(valor):
	return str(valor).replace("ó","o").replace("ú","u").replace("í","i").replace("á","a").replace("é","e")		
		
def tipo_v(tipo):
	if tipo ==str:
		return ""
	if tipo == int:
		return 0
	if tipo == bool:
		return False
	if tipo == None:
		return None
	if tipo == float:
		return 0.0
	if tipo == list:
		return []
	if tipo == tuple:
		return ()
	if tipo == dict:
		return {}

def tipo(cadena):
	cadena=cadena.replace("<type 'str'>","str")
	cadena=cadena.replace("<type 'int'>","int")
	cadena=cadena.replace("<type 'float'>","float")
	cadena=cadena.replace("<type 'list'>","list")
	cadena=cadena.replace("<type 'tuple'>","tuple")
	cadena=cadena.replace("<type 'None'>","None")
	cadena=cadena.replace("<type 'dict'>","dict")
	return cadena

def concatenar(lista,separador=None):
	i=""
	for elem in lista:
		if separador!=None:
			i+=str(elem)+separador
		else:
			i+=str(elem)
	if separador!=None:
			return i[:-1]
	else:
			return i
	
		
def concatenar2(lista):
	i=""
	for elem in lista:
		i+=str(elem)+"\n"
	return i
def posicionar(pantalla,t_posicion,posicion):
	pass

def arco(radio,lado="top"):
    r=radio
    t=1
    omega=(6.28)/t
    
    cosValue=math.cos(omega*t)
    sinValue=math.sin(omega*t)
    xPosition=(r*cosValue)
    yPosition=(r*sinValue)
    
    p=(int(xPosition),int(yPosition))	
    lista=[]
    p2=0
    while True:
		if p == p2:
			break 		
		t+=0.01
		cosValue=math.cos(omega*t)
		sinValue=math.sin(omega*t)
		xPosition=(r*cosValue)
		yPosition=(r*sinValue)	
		p2=(int(xPosition),int(yPosition))
		lista.append(p2)

		#print p2
		
    piesa=len(lista)/4
    print lista,"?????"
    
    if lado=="top":
		return lista
    if lado=="right":
		return lista[piesa:piesa*2]
    if lado=="bottom":
		return lista[piesa*2:piesa*3]
    if lado=="left":	
		return lista[piesa*3:piesa*4]	

def poligono(size,pos,radios):
	print radios
	if len(radios)==4:
		top=arco(radios[0],"top")
		add2(top,[pos[0],pos[1]])
		"""		
		right=arco(radios[1],"right")
		add2(right,[pos[0]+size[0]-(radios[1]+radios[2]),pos[1]+size[1]-(radios[0]+radios[3])])
		
		bottom=arco(radios[2],"bottom")
		add2(bottom,[pos[0],pos[1]+size[1]-(radios[3]+radios[2])])
		
		left=arco(radios[3],"left")
		add2(left,[pos[0],pos[1]])
		
		lista=top+right+bottom+left
		return lista
		"""			
		#print top,".........."	
		return top[:50]
	else:
		print "no hay los radios necesarios"	
	



		
	
def rect_radius(pos,size,radios,borde=False,inverso=False):
	angulo=0
	rect=[]
	right=[]
	bottom=[]
	left=[]
	top=[]

	while angulo < 6.4:
		sen=math.sin(angulo)
		cos=math.cos(angulo)
		if angulo<1.6:

			y=(sen*radios[2])+pos[1]+size[1]-radios[2]
			x=(cos*radios[2])+pos[0]+size[0]-radios[2]
			
			bottom.append((x,y))			
		if angulo>1.6 and angulo<3.2:

			y=(sen*radios[3])+pos[1]+size[1]-radios[3]
			x=(cos*radios[3])+pos[0]+radios[3]


			left.append((x,y))	
		if angulo>3.2 and angulo<4.8:

			y=(sen*radios[0])+pos[1]+radios[0]
			x=(cos*radios[0])+pos[0]+radios[0]
			
			top.append((x,y))	
			
		if angulo>4.8 and angulo<6.4:
			y=(sen*radios[1])+pos[1]+radios[1]
			x=(cos*radios[1])+pos[0]+size[0]-radios[1]
			right.append((x,y))
		

		angulo+=0.01
	if borde==False:
		rect=top+right+bottom+left
	else:
		rect=[top,right,bottom,left]
	if inverso == True:
		top.insert(0,(0,0))
		right.insert(0,(pos[0]+size[0],pos[1]))
		bottom.insert(0,(pos[0]+size[0],pos[1]+size[1]))
		left.insert(0,(pos[0],pos[1]+size[1]))
		rect=[top,right,bottom,left]

	
	return rect
	
def css_convert(atributo,css):
	if atributo in css:
		if atributo=="background" or atributo=="background-color":
			#css.atributos[atributo]
			return 2
	else:
		print "este atributo no existe"

def rect_radius2(pos,size,radios,borde=False,inverso=False):
	angulo=0#0
	rect=[]
	right=[]
	bottom=[]
	left=[]
	top=[]
	while angulo < 6.2:#6.4
		sen=math.sin(angulo)
		cos=math.cos(angulo)
		if angulo<1.6:
			y=int((sen*radios[2][1]))+pos[1]+size[1]-radios[2][1]
			x=int((cos*radios[2][0]))+pos[0]+size[0]-radios[2][0]

			
			bottom.append((x,y))			
		if angulo>1.6 and angulo<3.2:

			y=int((sen*radios[3][1]))+pos[1]+size[1]-radios[3][1]
			x=int((cos*radios[3][0]))+pos[0]+radios[3][0]-1
			left.append((x,y))	
		if angulo>3.2 and angulo<4.8:

			y=(sen*radios[0][1])+pos[1]+radios[0][1]
			x=(cos*radios[0][0])+pos[0]+radios[0][0]
			
			top.append((x,y))	
			
		if angulo>4.8 and angulo<6.2:
			y=(sen*radios[1][1])+pos[1]+radios[1][1]
			x=(cos*radios[1][0])+pos[0]+size[0]-radios[1][0]+1
			right.append((x,y))
		

		angulo+=0.002
	if borde==False:
		rect=top+right+bottom+left
	else:
		rect=[top,right,bottom,left]
	if inverso == True:
		top.insert(0,(0,0))
		right.insert(0,(pos[0]+size[0],pos[1]))
		bottom.insert(0,(pos[0]+size[0],pos[1]+size[1]))
		left.insert(0,(pos[0],pos[1]+size[1]))
		rect=[top,right,bottom,left]

	return rect
	
def separar(cadena):
	c=0
	start=0
	l=[]
	while c < len(cadena):
		if cadena[c] == "x" or cadena[c] == "%" or cadena[start:c+1] == "bottom" or cadena[start:c+1] == "right" or cadena[start:c+1] == "left" or  cadena[start:c+1] == "center" or cadena[start:c+1] == "top" or cadena[start:c+1] == "auto":
			if c<len(cadena):
				a=1
			else:
				a=0
			l.append(cadena[start:c+a])
			start=c+a
		c+=1
	
	return l

def css_posicionamiento(objetos):
	x=0
	y=0
	for elem in objetos:
		if elem.css.get_style("position") == "static":
			if elem.css.get_style("display")=="inline":
				pass
			if elem.css.get_style("display")=="block":
				pass
			if elem.css.get_style("display")=="inline-block":
				pass
			if elem.css.get_style("display")=="run-in":
				pass
			if elem.css.get_style("display")=="inline-table":
				pass
			if elem.css.get_style("display")=="table-footer-group":
				pass
			if elem.css.get_style("display")=="table-column":
				pass
			if elem.css.get_style("display")=="none":
				pass
			if elem.css.get_style("display")=="table-row-group":
				pass
			if elem.css.get_style("display")=="table-row":
				pass
			if elem.css.get_style("display")=="table-cell":
				pass
			if elem.css.get_style("display")=="inherit":
				pass
				
			if elem.css.get_style("display")=="list-item":
				pass
		
			if elem.css.get_style("display")=="table":
				pass
			if elem.css.get_style("display")=="table-header-group":
				pass
			if elem.css.get_style("display")=="table-column":
				pass
			if elem.css.get_style("display")=="table-caption":
				pass
			if elem.css.get_style("display")=="table-footer-group":
				pass
						
		if elem.css.get_style("position") == "relative":
			pass
			
		if elem.css.get_style("position") == "absolute":
			pass
			
		if elem.css.get_style("position") == "fixed":
			pass
		if elem.css.get_style("position") == "inherit":
			pass
			
def listar_d(dic,clave):
	l=[]
	elem=dic[clave]
	if elem !={}:
		for i in elem:
			if elem[i]!={}:
				elemento=elem[i]
				while elemento !={}:
					elemento
					
class dicc:
	def __init__(self):
		self.l_claves=[]
		self.d={}
		
		
	def niveles(self,clave,orden):
		contador=0
		if self.get(clave) !=None:
			ciclo=self.get(clave)
			while ciclo.keys_all() !=[]:
				if len(ciclo.keys_p)>=orden:
					try:
						ciclo=ciclo.get(ciclo.keys_p[orden])
						contador+=1
						
					except:
						break
		return contador
		
	def mapear(self,niveles=1):
		dic=self.d
		if niveles>20:
			niveles=20
		l=[]
		base="for elem0 in dic:\n try:\n  if dic[elem0].d.keys()!=[]:\n   l.append([elem0])\n   pass\n  else:\n   l.append([elem0])\n except:\n  l.append([elem0])"
		base2=base
		codigo=base
		lista="l.append([elem0])"
		for elem in range(niveles):
			if elem !=0:
				#base2=base2.replace("elem"+str(elem-1),"elem"+str(elem))
				base2=base2.replace("dic[elem0].d","dic"+diccionar_elem("elem",elem+1,".d"))
				base2=base2.replace("dic:","dic"+diccionar_elem("elem",elem,".d")+":")
				base2=base2.replace("for elem0","for elem"+str(elem))
				base2=base2.replace(lista,lista.replace("[elem0]",listar_elem("elem",elem+1)))
				base2=tabular(base2,get_tab2(codigo,"pass"))
				l_codigo=codigo.split("\n")
				for elem2 in l_codigo:
					if "pass" in elem2:
						l_codigo[l_codigo.index(elem2)]=base2
				codigo=concatenar2(l_codigo)
				base2=base
		f=open("/home/abraham/prueba.txt","w")
		f.write(codigo)
		f.close()
		exec(codigo)
		return l
	
			

				
				
				
				
					


			
					
		
			
				

			
					 
			
				
				
		
	#devuelve la clave del valor
	def get_keys(self,valor):
		for elem in self.keys_p():
			if self.d[elem]==valor:
				return self.keys(elem) 
			else:
				print "ese valor no se encuentra en el diccionario Z"
				return None
	#devuelve el valor de la clave
	def get(self,clave):
		indice=0
		for elem in self.l_claves:

			if clave in elem:
				indice=self.l_claves.index(elem)
				return self.d[self.l_claves[indice][0]]
		if not clave in elem:
				print "la clave no existe"
				return None
		
			
	#crea una lista de claves valor
	def set(self,valor,*claves):
		claves=list(claves)

		for elem in claves:
			if elem in self.keys_all():
				claves.remove(elem)
		if claves !=[]:
			self.l_claves.append(claves)
			self.d[claves[0]]=valor
			
		else:
			print "las claves ya estaban agragadas anteriormente"
	#crea una lista de claves valor
	def set2(self,valor,claves):
		claves2=list(claves)
		for elem in claves:
			if elem in self.keys_all():
				claves2.remove(elem)
			
		if claves !=[]:
			self.l_claves.append(claves2)
			self.d[claves2[0]]=valor
			
		else:
			print "las claves ya estaban agragadas anteriormente"			
	#agrega una lista de claves secundarias a la clave primaria
	def key2(self,clave,lista):
		claves=self.keys(clave)
		indice=self.l_claves.index(claves)
		for elem in lista:
			if not elem in self.l_claves[indice] and not elem in self.keys_all():
				 self.l_claves[indice].append(elem)
				 
	#agrega una clave secundaria a una clave primaria
	def key(self,clave1,clave2):
		for elem in self.l_claves:
			indice=self.l_claves.index(elem)
			self.l_claves[indice]=list(self.l_claves[indice])
			if clave1 in self.l_claves[indice] and not clave2 in self.keys_all():
				self.l_claves[indice].append(clave2)
	#devuelve una lista de claves secundarias de la clave primaria
	def keys(self,clave):
		for elem in self.l_claves:
			if clave in elem:
				indice=self.l_claves.index(elem)
		return self.l_claves[indice]
	
	#devuelve una lista de claves primarias 
	def keys_p(self):
		return self.d.keys()
	#muestra la clave primera de la clave secundaria
	def keys_p2(self,clave):
		for elem in self.l_claves:
			if clave in elem:
				return elem[0]
	#muestra todas las claves del diccionario
	def keys_all(self):
		l=[]
		for elem in self.l_claves:
			for elem2 in elem:
				l.append(elem2)
		return l
		
	#fusiona 2 diccionarios Z
	def fusionar(self,dic,sobrescribir=False):
		for elem in dic.keys_p():
			self.set2(dic.get(elem),dic.keys(elem))
		
		
		
				
	#muestra el diccionario Z completo	
	def show(self):
		print "<"
		for elem in self.l_claves:
			print elem,":",self.d[elem[0]]
		print ">"
#devuelve el numero de espacios y tabs
def get_tab(cadena,palabra):
	l=cadena.split("\n")
	columna=""
	for elem in l:
		if palabra in elem:
			 columna=elem
	x1=0
	x2=1               
	while columna[x1:x2]==" " or columna[x1:x2]=="	":
		x1+=1
		x2+=1
		
	return x1
#devuele una cadena con espacios y tabs
def get_tab2(cadena,palabra):
	l=cadena.split("\n")
	columna=""
	for elem in l:
		if palabra in elem:
			 columna=elem
	x1=0
	x2=1               
	while columna[x1:x2]==" " or columna[x1:x2]=="	":
		x1+=1
		x2+=1
		
	return columna[:x1]
	
def tabular(cadena,tabs):
	l=cadena.split("\n")
	if type(tabs)==str:
		for elem in l:
			l[l.index(elem)]=tabs+elem
	if type(tabs)==int:
		for elem in l:
			l[l.index(elem)]=" "*tabs+elem		
	cadena=""
	for elem in l:
		cadena+=elem+"\n"
	return cadena

#crea una lista con la palabra clave reptida con el numero de repeticion sumado a esta 
#ejemplo [elem0,elem1,elem2]
def listar_elem(palabra,numero):
	l=[]
	for elem in range(numero):
		l.append(palabra+str(elem))
	return str(l).replace("'","")
#crea un seguimento de claves para diccionarios
# ejemplo [elem0][elem1][elem2]
def diccionar_elem(palabra,numero,medio="",retorno=0):
	l=[]
	cadena=""
	for elem in range(numero):
		l.append(palabra+str(elem))
	for elem in l:
		cadena+="["+elem+"]"+medio
	if retorno >0:
		return cadena[:-retorno]
	elif retorno<0:
		return cadena[:retorno]
	elif retorno==0:	
		return cadena	
		
#muestra una lista de las convinaciones de las claves del diccionario hasta un maximo de 20 niveles
def mapear(dic,niveles=1,mapeo="claves"):
	if niveles>20:
		niveles=20
	l=[]
	base="for elem0 in dic:\n if type(dic[elem0])==dict:\n  if dic[elem0].keys()!=[]:\n   l.append([elem0])\n   pass\n  else:\n   l.append([elem0])\n else:\n  l.append([elemento])"
	base2=base
	codigo=base
	lista="l.append([elem0])"
	for elem in range(niveles):
		if elem !=0:
			#base2=base2.replace("elem"+str(elem-1),"elem"+str(elem))
			base2=base2.replace("dic[elem0]","dic"+diccionar_elem("elem",elem+1))
			base2=base2.replace("dic:","dic"+diccionar_elem("elem",elem)+":")
			base2=base2.replace("for elem0","for elem"+str(elem))
			base2=base2.replace(lista,lista.replace("[elem0]",listar_elem("elem",elem+1)))
			if mapeo=="claves":
				base2=base2.replace("([elemento])","(["+listar_elem("elem",elem+1)+"])")
			if mapeo=="valores":
				base2=base2.replace("([elemento])","("+listar_elem("elem",elem+1)[:-1]+",dic"+diccionar_elem("elem",elem+1)+"])")				
			base2=tabular(base2,get_tab2(codigo,"pass"))
			l_codigo=codigo.split("\n")
			for elem2 in l_codigo:
				if "pass" in elem2:
					l_codigo[l_codigo.index(elem2)]=base2
			codigo=concatenar2(l_codigo)
			base2=base

	exec(codigo)
	return l
		
def buscar_ruta(dic,palabra,niveles=1,todo="todo",mapeo="claves"):
	l=mapear(dic,niveles,mapeo)
	l_temp=[]
	l_remover=[]
	for elem in l:
		if elem.count(palabra)>=1:

			l_temp.append(elem)	
	if mapeo=="calves":
		if todo=="solo":#devuelve toda la ruta a seguir hasta palabra
			for elem in l_temp:
				if elem[len(elem)-1]!=palabra:
					l_remover.append(elem)
			for elem in l_remover:
				l_temp.remove(elem)
				
		if todo=="claves ruta":
			for elem in l_temp:
				if elem[len(elem)-2]!=palabra:
					l_remover.append(elem)
			for elem in l_remover:
				l_temp.remove(elem)
		if todo=="claves":#devuelve las claves de la palabra
			
			for elem in l_temp:
				if elem[len(elem)-1]!=palabra and elem[len(elem)-2]==palabra:
					l_remover.append(elem[len(elem)-1])
			l_temp=l_remover
			
		if todo=="padre":#devuelve el clave padre de la palabra
			for elem in l_temp:
					l_temp=[]
					if palabra in elem:
						indice=elem.index(palabra)
						if indice>0:
					
							l_temp.append(elem[indice-1])	
	if mapeo=="valores":
		if todo=="solo":#devuelve toda la ruta a seguir hasta palabra
			l2=[]
			for elem in l_temp:
				if elem[len(elem)-1]==palabra:

					l2.append(elem)
			l_temp=l2
	return l_temp



def unir_key_map(lista):
	l=[]
	for elem in lista:
		if len(elem)>0:
			l.append(elem[1])
		else:
			l.append(elem[0])
	return l

"""
d={1:{},
   2:{11:"hola",12:{}},
   3:{6:{8:{},7:{}}},
   4:{9:{10:{}}},
   5:{},
	}

print buscar_ruta(d,10,15,"padre")
"""
def estaEn(lista,cadena):
	for elem in lista:
		if elem in lista:
			return True
	return False

def movPosList(l,posActual,nuevaPos):
	lista=l
	elem=lista[posActual]
	del lista[posActual]
	lista.insert(nuevaPos,elem)
	return lista


def movPosStr(cadena,posActual,nuevaPos):
	espacio=""
	palabra=""
	espacios=[]
	palabras=[]
	c=0
	primero=None
	while c<len(cadena):
		
		if cadena[c]==" " or cadena[c]=="\n" or cadena[c]=="\t":				
				espacio+=cadena[c]
				if primero==None:
					primero=True
		
		else:
			if espacio!="":
				espacios.append(espacio)
				espacio=""			
		if cadena[c]!=" " and cadena[c]!="\n" and cadena[c]!="\t":
				palabra+=cadena[c]
				if primero==None:
					primero=False
		else:
			palabras.append(palabra)
			palabra=""
		print "cadena: ",[cadena[c]]
		print palabra
		print espacio						
		c+=1
	if palabra !="":
		palabras.append(palabra)
	if espacio!="":
		espacios.append(espacio)
	
	
	palabras=movPosList(palabras,posActual,nuevaPos)
	print palabras
	cadena=""
	if primero==True:
		c=0
		while c<len(espacios):
			cadena+=espacios[c]
			if c<len(palabra):
				cadena+=palabras[c]
			c+=1
	elif primero==False:
		c=0
		while c<len(palabras):
			cadena+=palabras[c]
			if c<len(espacios):
				cadena+=espacios[c]
			c+=1
	return cadena