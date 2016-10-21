#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ZerpaCorp import zu
import pygame

class CSS:
	def __init__(self,pantalla=None):
		self.subpantalla=None
		self.pantalla=pantalla
		self.pos_relativa=[0,0]
		self.tipo=None
		self.superficie=None
		self.superficie_oculta=None
		self.atributos={
			"color":"rgba(0,0,0,1)",#color de las letras
			"font-size":"12px",#tamaño de las letras
			"font-family":"none",#la familia de la tipografia
			"font-weight":"normal",#ensancha las letras
			"font-style":"normal",#estilo de las letras(normal o cursiva)
			"line-height":"",#alto de una linea
			"text-decoration":"",#la decoracion del texto
			"text-align":"",#la alineacion del texto
			"text-indent":"",#sagrado o margenes
			"text-transform":"",#transforma el texto 
			"background":"rgba(255,255,255,0)",#color de fondo
			"background-color":"rgba(255,255,255,0)",#color de fondo
			"background-image":"none",#imagen de fondo
			"background-repeat":"repeat",#imagen de fondo
			"background-position":"0px 0px",#posicion de la imagen
			"background-size":"auto auto",
			
			"margin":"0px 0px 0px 0px",#tamaño de todos los margins
			"margin-left":"0px",#tamaño del margen izquierdo
			"margin-right":"0px",#tamaño del margen derecho
			"margin-top":"0px",#tamaño del margen superior
			"margin-bottom":"0px",#tamaño del margen inferior
			"margin-color":"none",#color del margin
			
			"padding-left":"0px",#tamaño del padding izquierdo
			"padding-right":"0px",#tamaño del padding derecho
			"padding-top":"0px",#tamaño del padding superior
			"padding-botton":"0px",#tamaño del padding inferior
			"padding":"0px 0px 0px 0px",#tamaño de todos los paddings
			"padding-color":"none",#color del padding
			
			"border":"none",
			"border-color":"rgba(0,0,0,0)",#color del borde
			"border-style":"none",#estilo del borde
			"border-left-color":"rgba(0,0,0,0)",
			"border-top-color":"rgba(0,0,0,0)",
			"border-right-color":"rgba(0,0,0,0)",
			"border-bottom-color":"rgba(0,0,0,0)",
			
			"border-width":"0px",#tamaño del borde
			"border-left":"0px",#tamaño del borde
			"border-right":"0px",#tamaño del borde
			"border-top":"0px",#tamaño del borde			
			"border-bottom":"0px",#tamaño del borde
			
			"border-radius":"0px 0px 0px 0px",
			"border-bottom-right-radius":"0px 0px",
			"border-bottom-left-radius":"0px 0px",
			"border-top-right-radius":"0px 0px",
			"border-top-left-radius":"0px 0px",
			
			
			"float":"none",#alinea un elemento
			"clear":"",#
			"width":"100%",#ancho
			"height":"auto",#alto
			"position":"static",#posicion
			"left":"0px",
			"top":"0px",
			"overflow":"visible",
			"overflow-y":"visible",
			"overflow-x":"visible",
			"display":"block",
			"resize":"none"
			
			}
		self.pantalla=None
		
	def get_style(self,atributo):
		if atributo in self.atributos:
			if atributo=="font-size":
				return int(self.atributos[atributo].replace("px",""))
				
			if atributo=="background-position":
				l=[]		
				
			if atributo=="display":
				return self.atributos[atributo] 
			
			if atributo=="background" or atributo=="background-color" or atributo=="color" or atributo=="border-top-color" or atributo=="border-left-color" or atributo=="border-bottom-color" or atributo=="border-right-color" or  atributo=="background-image":
				if "rgba" in self.atributos[atributo]:
					valor=self.atributos[atributo].replace("rgba(","").replace(")","").split(",")
					valor[3]=float(valor[3])*255
					return (int(valor[0]),int(valor[1]),int(valor[2]),valor[3])
					
				if "url" in self.atributos[atributo]:
						superficie=pygame.Surface((self.get_style("width"),self.get_style("height"))).convert_alpha()
						superficie.fill((0,0,0,0))		
						imagenes=self.atributos[atributo].split(",")
						imagenes.reverse()
						repeticiones=self.atributos["background-repeat"].split(",")
						sizes=[]
						posicion=[]

																			
						while len(repeticiones) < len(imagenes):
							repeticiones.append("repeat")
						repeticiones.reverse()
			
						c=0
						for elem in self.atributos["background-position"].replace(" ","").split(","):
							pos=zu.separar(elem)
							posicion.append(pos)
						for elem in self.atributos["background-size"].split(","):
							size=zu.separar(elem.replace(" ",""))
							sizes.append(size)
							
							
						
						

						while len(sizes) < len(imagenes):
							sizes.append(["auto","auto"])
						sizes.reverse()
						
						
						while len(posicion) < len(imagenes):
							posicion.append([0,0])	
													
						posicion.reverse()
						for elem in imagenes:
							if "http:" in self.atributos[atributo]:
								pass
							else:
								s=pygame.Surface((self.get_style("width"),self.get_style("height"))).convert_alpha()
								s.fill((0,0,0,0))
								valor=elem.replace("url(","").replace(")","")
								img=pygame.image.load(valor).convert_alpha()
								if "px" in str(sizes[c][0]):
									sizes[c][0]=int(sizes[c][0].replace("px",""))
								if "%" in str(sizes[c][0]):
									sizes[c][0]=(int(sizes[c][1].replace("%",""))*self.get_style("width"))/100
								if "px" in str(sizes[c][1]):
									sizes[c][1]=int(sizes[c][1].replace("px",""))
								if "%" in str(sizes[c][1]):
									sizes[c][1]=(int(sizes[c][1].replace("%",""))*self.get_style("height"))/100									
								
								if sizes[c][0]=="auto" and sizes[c][1]!="auto":
									img=pygame.transform.scale(img,(img.get_width(),sizes[c][1]))
									
								elif sizes[c][1]=="auto" and sizes[c][0]!="auto":
									img=pygame.transform.scale(img,(sizes[c][0],img.get_height()))
								elif sizes[c][1]!="auto" and sizes[c][0]!="auto" :
									img=pygame.transform.scale(img,(sizes[c][0],sizes[c][1]))
									
									
									
																
								if posicion[c][0]=="center":
									posicion[c][0]=(self.get_style("width")/2)-(img.get_width()/2)
								elif posicion[c][0]=="left":
									posicion[c][0]=0		
								elif posicion[c][0]=="right":
									posicion[c][0]=self.get_style("width")-img.get_width()
								else:
									if "px" in str(posicion[c][0]):
										posicion[c][0]=int(posicion[c][0].replace("px",""))
									elif "%" in str(posicion[c][0]):
										posicion[c][0]=	(int(posicion[c][0].replace("%",""))*self.get_style("width"))/100	
													
								if posicion[c][1]=="center":
									posicion[c][1]=(self.get_style("height")/2)-(img.get_height()/2)
									
								elif posicion[c][1]=="top":
									posicion[c][1]=0
								elif posicion[c][1]=="bottom":
									posicion[c][1]=self.get_style("height")-img.get_height()
								else:
									if "px" in str(posicion[c][1]):
										posicion[c][1]=int(posicion[c][1].replace("px",""))
									elif "%" in str(posicion[c][1]):
										posicion[c][1]=	(int(posicion[c][1].replace("%",""))*self.get_style("height"))/100
								
								

							
								x=0
								y=0
								valorx=0
								
								if repeticiones[c]=="repeat":
									if posicion[c][0] >0:
										cantidad=((posicion[c][0]/img.get_width())+1)
										valorx=posicion[c][0]-(img.get_width()*cantidad)
										x=valorx
										
									if posicion[c][1] >0:
										cantidad=((posicion[c][1]/img.get_height())+1)
										valory=posicion[c][1]-(img.get_height()*cantidad)
										y=valory
									
									while y<self.get_style("height"):
										while x<self.get_style("width"):
											s.blit(img,(x,y))
											x+=img.get_width()
										x=valorx
										y+=img.get_height()
									superficie.blit(s,(0,0))
									
								if repeticiones[c]=="repeat-x":
									if posicion[c][1] >0:
										cantidad=((posicion[c][0]/img.get_width())+1)
										valorx=posicion[c][0]-(img.get_width()*cantidad)
										x=valorx

										while x<self.get_style("width"):
											s.blit(img,(x,posicion[c][1]))
											x+=img.get_width()
										superficie.blit(s,(0,0))
										
								if repeticiones[c]=="repeat-y":
									if posicion[c][1] >0:
										cantidad=((posicion[c][1]/img.get_height())+1)
										valory=posicion[c][1]-(img.get_height()*cantidad)
										y=valory

									while y<self.get_style("height"):
											s.blit(img,(posicion[c][0],y))
											y+=img.get_height()
									superficie.blit(s,(0,0))
								if repeticiones[c]=="no-repeat":
									superficie.blit(img,(posicion[c][0],posicion[c][1]))
									
							c+=1	
						return  superficie										
					
				
				
			if atributo=="border-width" or atributo=="border-top" or atributo=="border-right" or atributo=="border-bottom" or atributo=="border-left":
				valor=int(self.atributos[atributo].replace("px",""))
				return valor
				
			if atributo=="position":
				return  self.atributos[atributo]
			#tamaño y posición	
			if atributo=="top" or atributo=="left" or atributo=="width" or atributo=="height" :
				if "px" in self.atributos[atributo]:
					valor=int(self.atributos[atributo].replace("px",""))
					if self.atributos["position"]=="static":
						if atributo=="top":
							valor=self.pos_relativa[1]
						if atributo=="left":
							valor=self.pos_relativa[0]			
											
					if self.atributos["position"]=="relative":
						if atributo=="top":
							valor=valor+self.pos_relativa[1]+self.get_style("margin-top")
						if atributo=="left":
							valor=valor+self.pos_relativa[0]+self.get_style("margin-left")
							
					if self.atributos["position"]=="absolute":
						if atributo=="top":
							valor=valor+self.get_style("margin-top")
						if atributo=="left":
							valor=valor+self.get_style("margin-left")	
					return valor
					
					
				if "%" in self.atributos[atributo]:
					
					if self.pantalla!=None:
						valor=int(self.atributos[atributo].replace("%",""))
							
						if atributo=="top" or atributo=="height" or atributo=="margin-top" or atributo=="margin-bottom" :
							
							valor=(int(valor)*self.pantalla.get_height())/100
							if self.atributos["position"]=="none":
								if atributo=="top":
									valor=0
							return valor
						if atributo=="left" or atributo=="width" or atributo=="margin-left" or atributo=="margin-right" :
							
							valor=(int(valor)*self.pantalla.get_width())/100
							if self.atributos["position"]=="none":
								if atributo=="left":
									valor=0					
							return valor	
							
				if self.atributos[atributo]=="auto":
						if atributo=="height" and self.subpantalla==None:
							valor=0
						if atributo=="height" and self.subpantalla!=None:
							valor=self.subpantalla.get_height()		

						if atributo=="width" and self.subpantalla==None:
							valor=0
						if atributo=="width" and self.subpantalla!=None:
							valor=self.subpantalla.get_width()	
						return valor
				

										
			if atributo=="border-radius" or atributo=="border-top-left-radius" or atributo=="border-top-right-radius" or atributo=="border-bottom-right-radius" or atributo=="border-bottom-left-radius":
				top=self.atributos["border-top-left-radius"]
				right=self.atributos["border-top-right-radius"]
				bottom=self.atributos["border-bottom-right-radius"]
				left=self.atributos["border-bottom-left-radius"]
				if "%" in top:
					top=[zu.ciento(int(top.replace("%","")),self.get_style("width")),zu.ciento(int(top.replace("%","")),self.get_style("height"))]
				else:
					top=zu.separar(top)
					top[0]=int(top[0].replace("px",""))
					top[1]=int(top[1].replace("px",""))
					
				if "%" in right:
					right=[zu.ciento(int(right.replace("%","")),self.get_style("width")),zu.ciento(int(right.replace("%","")),self.get_style("height"))]
				else:
					right=zu.separar(right)
					right[0]=int(right[0].replace("px",""))
					right[1]=int(right[1].replace("px",""))
				if "%" in bottom:
					bottom=[zu.ciento(int(bottom.replace("%","")),self.get_style("width")),zu.ciento(int(bottom.replace("%","")),self.get_style("height"))]
				else:
					
					bottom=zu.separar(bottom)
					bottom[0]=int(bottom[0].replace("px",""))
					bottom[1]=int(bottom[1].replace("px",""))
				if "%" in left:
					
					left=[zu.ciento(int(left.replace("%","")),self.get_style("width")),zu.ciento(int(left.replace("%","")),self.get_style("height"))]
				else:

					left=zu.separar(left)
					left[0]=int(left[0].replace("px",""))
					left[1]=int(left[1].replace("px",""))
					
				if atributo=="border-radius":
					return [top,right,bottom,left]
				if atributo=="border-bottom-left-radius":
					return left
				if atributo=="border-top-left-radius":
					return top
				if atributo=="border-bottom-right-radius":
					return bottom
				if atributo=="border-top-right-radius":
					return right
					
			if atributo=="margin" or atributo=="margin-top" or atributo=="margin-right" or atributo=="margin-bottom" or atributo=="margin-left":

				top=self.atributos["margin-top"]
				right=self.atributos["margin-right"]
				bottom=self.atributos["margin-bottom"]
				left=self.atributos["margin-left"]
				if "%" in top:
					top=zu.ciento(int(top.replace("%","")),self.pantalla.get_height())
				else:
					top=int(top.replace("px",""))
				if "%" in right:
					right=zu.ciento(int(right.replace("%","")),self.pantalla.get_width())
				else:
					right=int(right.replace("px",""))
				if "%" in bottom:
					bottom=zu.ciento(int(bottom.replace("%","")),self.pantalla.get_height())
				else:
					bottom=int(bottom.replace("px",""))
				if "%" in left:
					left=zu.ciento(int(left.replace("%","")),self.pantalla.get_width())
				else:
					left=int(left.replace("px",""))
				if atributo=="margin":
					return [top,right,bottom,left]
				if atributo=="margin-left":
					return left
				if atributo=="margin-top":
					return top
				if atributo=="margin-bottom":
					return bottom
				if atributo=="margin-right":
					return right				
			if atributo=="overflow" and self.atributos["overflow"]=="scroll":
		 		return [self.atributos["overflow-x"],self.atributos["overflow-y"]]
			if atributo=="overflow" and self.atributos["overflow"]=="visible":	
				return "visible"
			if atributo=="overflow" and self.atributos["overflow"]=="hidden":	
				return "hidden"						
			if 	atributo=="border-top" or atributo=="border-right" or atributo=="border-bottom" or atributo=="border-left":
				return int(self.atributos[atributo].replace("px",""))
		else:
			print "el atributo "+atributo+" no existe"
			return None
			
		
	def set_style(self,atributo,valor):
			if atributo=="font-size" and "px" in valor:
					self.atributos[atributo]=valor
			if atributo=="background-position":
				if "center" in valor or "px" in valor or "left" in valor or "right" in valor or "bottom" in valor or "top" in valor or "," in valor or "%" in valor:
					self.atributos[atributo]=valor
			if atributo=="background-size":
				if "%" in valor or "px" in valor or "auto" in valor or "," in valor:
					self.atributos[atributo]=valor				
				
				
				
			if atributo=="display":
				self.atributos[atributo]=valor
			if atributo=="background-repeat":
				if valor=="repeat" or valor=="repeat-x" or valor=="repeat-y" or valor=="no-repeat" or "," in valor:
					self.atributos[atributo]=valor
			if atributo=="background" or atributo=="background-color" or atributo=="color" or atributo=="border-top-color" or atributo=="border-left-color" or atributo=="border-bottom-color" or atributo=="border-right-color" or atributo=="background-image":
				if "rgb(" in valor:
					color=valor.replace("rgb(","")
					color=valor.replace(")","")
					color=color.split(",")
					valor="rgba("+color[0]+","+color[1]+","+color[2]+","+"1"+")"
				
				
				self.atributos[atributo]=valor
				if "url(" in valor:
					self.atributos["background-image"]=valor
			
				
			
			if atributo=="margin-top":
				self.atributos["margin-top"]=valor
				lista=self.atributos["margin"].split(" ")
				lista[0]=valor
				lista=self.atributos["margin"]=zu.concatenar(lista)
				
			if atributo=="margin-right":
				self.atributos["margin-right"]=valor
				lista=self.atributos["margin"].split(" ")
				lista[1]=valor
				lista=self.atributos["margin"]=zu.concatenar(lista)				

			if atributo=="margin-bottom":
				self.atributos["margin-bottom"]=valor
				lista=self.atributos["margin"].split(" ")
				lista[2]=valor
				lista=self.atributos["margin"]=zu.concatenar(lista)

			if atributo=="margin-left":
				self.atributos["margin-left"]=valor
				lista=self.atributos["margin"].split(" ")
				lista[3]=valor
				lista=self.atributos["margin"]=zu.concatenar(lista)

			if atributo=="padding-top":
				self.atributos["padding-top"]=valor
				lista=self.atributos["padding"].split(" ")
				lista[0]=valor
				lista=self.atributos["padding"]=zu.concatenar(lista)
				
			if atributo=="padding-right":
				self.atributos["padding-right"]=valor
				lista=self.atributos["padding"].split(" ")
				lista[1]=valor
				lista=self.atributos["padding"]=zu.concatenar(lista)				

			if atributo=="padding-bottom":
				self.atributos["padding-bottom"]=valor
				lista=self.atributos["padding"].split(" ")
				lista[2]=valor
				lista=self.atributos["padding"]=zu.concatenar(lista)

			if atributo=="padding-left":
				self.atributos["padding-left"]=valor
				lista=self.atributos["padding"].split(" ")
				lista[3]=valor
				lista=self.atributos["padding"]=zu.concatenar(lista)
			#-----------------------------------------------------------			

			if atributo=="margin":
				lista=valor.split(" ")

				if len(lista) ==4:
					self.atributos["margin-top"]=lista[0]
					self.atributos["margin-right"]=lista[1]
					self.atributos["margin-bottom"]=lista[2]
					self.atributos["margin-left"]=lista[3]
					self.atributos["margin"]=self.atributos["padding-top"]+" "+self.atributos["padding-right"]+" "+self.atributos["padding-bottom"]+" "+self.atributos["padding-left"]
				elif len(lista) ==3:
					self.atributos["margin-top"]=lista[0]
					self.atributos["margin-right"]=lista[1]
					self.atributos["margin-bottom"]=lista[2]
					self.atributos["margin"]=self.atributos["padding-top"]+" "+self.atributos["padding-right"]+" "+self.atributos["padding-bottom"]+" "+self.atributos["padding-right"]
				elif len(lista) ==2:
					self.atributos["margin-top"]=lista[0]
					self.atributos["margin-right"]=lista[1]
					self.atributos["margin"]=self.atributos["margin-top"]+" "+self.atributos["margin-right"]+" "+self.atributos["margin-top"]+" "+self.atributos["margin-right"]				
				elif len(lista) ==1:
					self.atributos["margin-top"]=lista[0]
					self.atributos["margin"]=self.atributos["margin-top"]+" "+self.atributos["margin-top"]+" "+self.atributos["margin-top"]+" "+self.atributos["margin-top"]
				
			if atributo=="padding":
				lista=valor.split(" ")
				while " " in lista:
					lista.remove(" ")
				if len(lista) ==4:
					self.atributos["padding-top"]=lista[0]
					self.atributos["padding-right"]=lista[1]
					self.atributos["padding-bottom"]=lista[2]
					self.atributos["padding-left"]=lista[3]
					self.atributos["padding"]=self.atributos["padding-top"]+" "+self.atributos["padding-right"]+" "+self.atributos["padding-bottom"]+" "+self.atributos["padding-left"]
				elif len(lista) ==3:
					self.atributos["padding-top"]=lista[0]
					self.atributos["padding-right"]=lista[1]
					self.atributos["padding-bottom"]=lista[2]
					self.atributos["padding"]=self.atributos["padding-top"]+" "+self.atributos["padding-right"]+" "+self.atributos["padding-bottom"]+" "+self.atributos["padding-right"]
				elif len(lista) ==2:
					self.atributos["padding-top"]=lista[0]
					self.atributos["padding-right"]=lista[1]
					self.atributos["padding"]=self.atributos["padding-top"]+" "+self.atributos["padding-right"]+" "+self.atributos["padding-top"]+" "+self.atributos["padding-right"]
				elif len(lista) ==1:
					self.atributos["padding-top"]=lista[0]
					self.atributos["padding"]=self.atributos["padding-top"]+" "+self.atributos["padding-top"]+" "+self.atributos["padding-top"]+" "+self.atributos["padding-top"]
			if atributo=="border":
				if valor=="solid":
					self.atributos["border-width"]="3px"
					self.atributos["border-top"]=self.atributos["border-width"]
					self.atributos["border-right"]=self.atributos["border-width"]
					self.atributos["border-bottom"]=self.atributos["border-width"]
					self.atributos["border-left"]=self.atributos["border-width"]					
			if atributo=="border-width":
				self.atributos["border-width"]=valor
				self.atributos["border-top"]=self.atributos["border-width"]
				self.atributos["border-right"]=self.atributos["border-width"]
				self.atributos["border-bottom"]=self.atributos["border-width"]
				self.atributos["border-left"]=self.atributos["border-width"]	
				
			if atributo=="position":
				if "px" in valor or "%" in valor or "," in valor or "auto":
					self.atributos["position"]=valor	
								
			if atributo=="position":
				self.atributos["position"]=valor	
				
			if atributo=="position":
				self.atributos["position"]=valor	
			if atributo=="width":
				self.atributos["width"]=valor					
			if atributo=="height":
				self.atributos["height"]=valor
			if atributo=="top":
				self.atributos["top"]=valor
			if atributo=="left":
				self.atributos["left"]=valor
			if atributo=="border-radius":
				valor=zu.separar(valor)
				c=0
				for elem in valor:
					
					if "%" in elem:
						if int(elem.replace("%","")) > 50:
							valor[c]="50%"
					c+=1
					
				if len(valor) == 1:
					radios=valor[0].replace(" ","")+" "+ valor[0].replace(" ","")+" "+valor[0].replace(" ","")+" "+valor[0].replace(" ","")
					if "px" in valor[0]:
						self.atributos["border-top-left-radius"]=valor[0].replace(" ","")+" "+valor[0].replace(" ","")
						self.atributos["border-top-right-radius"]=valor[0].replace(" ","")+" "+valor[0].replace(" ","")
						self.atributos["border-bottom-left-radius"]=valor[0].replace(" ","")+" "+valor[0].replace(" ","")
						self.atributos["border-bottom-right-radius"]=valor[0].replace(" ","")+" "+valor[0].replace(" ","")
						
					if "%" in valor[0]:
						self.atributos["border-top-left-radius"]=valor[0].replace(" ","")
						self.atributos["border-top-right-radius"]=valor[0].replace(" ","")
						self.atributos["border-bottom-left-radius"]=valor[0].replace(" ","")
						self.atributos["border-bottom-right-radius"]=valor[0].replace(" ","")
				if len(valor) == 2:
					radios=valor[0].replace(" ","")+" "+ valor[1].replace(" ","")+" "+valor[0].replace(" ","")+" "+valor[1].replace(" ","")	
					if "px" in valor[0]:
						self.atributos["border-top-left-radius"]=valor[0].replace(" ","")+" "+valor[0].replace(" ","")
						self.atributos["border-bottom-right-radius"]=valor[1].replace(" ","")+" "+valor[0].replace(" ","")
					if "%" in valor[0]:
						self.atributos["border-top-left-radius"]=valor[0].replace(" ","")
						self.atributos["border-bottom-right-radius"]=valor[1].replace(" ","")
												
					if "px" in valor[1]:
						self.atributos["border-top-right-radius"]=valor[1].replace(" ","")+" "+valor[1].replace(" ","")
						self.atributos["border-bottom-left-radius"]=valor[0].replace(" ","")+" "+valor[1].replace(" ","")
						
					if "%" in valor[1]:
						self.atributos["border-top-right-radius"]=valor[1].replace(" ","")
						self.atributos["border-bottom-left-radius"]=valor[0].replace(" ","")
				if len(valor) == 3:
					radios=valor[0].replace(" ","")+" "+ valor[1].replace(" ","")+" "+valor[2].replace(" ","")+" "+valor[1].replace(" ","")

					if "px" in valor[0]:
						self.atributos["border-top-left-radius"]=valor[0].replace(" ","")+" "+valor[0].replace(" ","")
					if "%" in valor[0]:
						self.atributos["border-top-left-radius"]=valor[0].replace(" ","")

												
					if "px" in valor[1]:
						self.atributos["border-top-right-radius"]=valor[1].replace(" ","")+" "+valor[1].replace(" ","")
						self.atributos["border-bottom-left-radius"]=valor[1].replace(" ","")+" "+valor[1].replace(" ","")
						
					if "%" in valor[1]:
						self.atributos["border-top-right-radius"]=valor[1].replace(" ","")
						self.atributos["border-bottom-left-radius"]=valor[1].replace(" ","")					
					
					if "px" in valor[2]:
						self.atributos["border-bottom-right-radius"]=valor[2].replace(" ","")+" "+valor[2].replace(" ","")
						
					if "%" in valor[2]:
						self.atributos["border-bottom-right-radius"]=valor[2].replace(" ","")				
					
					
					
					
					
					
					
				if len(valor) == 4:
					radios=valor[0].replace(" ","")+" "+ valor[1].replace(" ","")+" "+valor[2].replace(" ","")+" "+valor[3].replace(" ","")	
					if "px" in valor[0]:
						self.atributos["border-top-left-radius"]=valor[0].replace(" ","")+" "+valor[0].replace(" ","")
					if "%" in valor[0]:
						self.atributos["border-top-left-radius"]=valor[0].replace(" ","")

												
					if "px" in valor[1]:
						self.atributos["border-top-right-radius"]=valor[1].replace(" ","")+" "+valor[1].replace(" ","")

						
					if "%" in valor[1]:
						self.atributos["border-top-right-radius"]=valor[1].replace(" ","")
										
					if "px" in valor[2]:
						self.atributos["border-bottom-right-radius"]=valor[2].replace(" ","")+" "+valor[2].replace(" ","")
						
					if "%" in valor[2]:
						self.atributos["border-bottom-right-radius"]=valor[2].replace(" ","")
								
					if "px" in valor[3]:

						self.atributos["border-bottom-left-radius"]=valor[3].replace(" ","")+" "+valor[3].replace(" ","")
						
					if "%" in valor[3]:
						self.atributos["border-bottom-left-radius"]=valor[3].replace(" ","")	
						
				self.atributos["border-radius"]=radios
			if valor=="scroll" or valor=="auto" or valor=="visible" or valor=="hidden" :
				if atributo=="overflow" and valor=="visible":
					self.atributos["overflow"]=valor
				if atributo=="overflow" and valor=="hidden":
					self.atributos["overflow"]=valor
				if atributo=="overflow" and valor=="auto":
					self.atributos["overflow"]=valor
				if atributo=="overflow" and valor=="scroll":
					self.atributos["overflow"]=valor
					self.atributos["overflow-x"]=valor
					self.atributos["overflow-y"]=valor
					bordes=zu.separar(self.atributos["border-radius"])
					bordes[1]="0px"
					bordes[2]="0px"
					bordes[3]="0px"
					
					self.atributos["border-radius"]=zu.concatenar(bordes)
					self.atributos["border-top-right-radius"]="0px 0px"
					self.atributos["border-bottom-right-radius"]="0px 0px"
					self.atributos["border-bottom-left-radius"]="0px 0px"
					
				if atributo=="overflow-x":		
					self.atributos["overflow-x"]=valor
					bordes=zu.separar(self.atributos["border-radius"])
					bordes[2]="0px"
					bordes[3]="0px"		
					self.atributos["border-radius"]=zu.concatenar(bordes)							
				if atributo=="overflow-y":		
					self.atributos["overflow-y"]=valor
					bordes=zu.separar(self.atributos["border-radius"])
					bordes[1]="0px"
					bordes[2]="0px"
					self.atributos["border-radius"]=zu.concatenar(bordes)	
							
	def update(self,pantalla):
		self.pantalla=pantalla
		
	def dibujar(self,app,objetos):
		print objetos,"objetos"
		for elem in objetos[0]:
			app.obj_pygame[elem].css.superficie.blit(self.superficie,(self.get_style("left")+app.obj_pygame[elem].css.get_style("border-left"),self.get_style("top")+app.obj_pygame[elem].css.get_style("border-top")))
			

