#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ZerpaCorp.Z as Z
import pygameGUI.app.Div.div as div
import pygameGUI.app.Letra.letra as letra

import pygameGUI
Z2=Z.Z("Z2")

codigo1="""
		import ZerpaCorp.zu as zu
		import random
		pygame.init() # inicializo el modulo
		# fijo las dimensiones de la pantalla a 300,300 y creo una superficie que va ser la principal
		pantalla=pygame.display.set_mode((0,0),RESIZABLE)
		modo=True
		pygame.display.set_caption(Z2.app) # Titulo de la Ventana
		#creo un reloj para controlar los fps
		reloj1=pygame.time.Clock()
		c=0
		blanco=(255,255,255) # color blanco en RGB
		salir=False
		fuente1=pygame.font.SysFont("Arial",30)
		pantalla_completa=(pygame.display.Info().current_w,pygame.display.Info().current_h)
		size_ventana=(800,600)
		color=255
		renderizador=True
		
		#LOOP PRINCIPAL
		while salir!=True:
			#recorro todos los eventos producidos
			#en realidad es una lista
			for event in pygame.event.get():
				# pygame.QUIT( cruz de la ventana)
				if event.type == pygame.QUIT:
					salir=True
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_ESCAPE:
						salir=True
					if event.key==pygame.K_c:
						print modo
						print pygame.display.get_driver()
						if modo==True:
							modo=False
							pantalla=pygame.display.set_mode(pantalla_completa,HWSURFACE|DOUBLEBUF)
							pantalla=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
						else:
							del pantalla
							pantalla=pygame.display.set_mode(size_ventana,RESIZABLE)
							modo=True
						
						
							
						
						#pygame.display.toggle_fullscreen()					
						#print pygame.display.get_heigth()
					#print pygame.key.name(event.key)
					#print event.key
					#print dir(event.key)
					
				if event.type==VIDEORESIZE:
					
					pantalla=pygame.display.set_mode(event.dict['size'],RESIZABLE)
					renderizador=True
					pygame.display.flip()
					
				
				# si el evento es del tipo        
			reloj1.tick(24)#operacion para que todo corra a 24fps
			pantalla.fill(blanco) # pinto la superficie de blanco
			#-----------------------------------------------------------
			s_pantalla=pygame.Surface((pygame.display.Info().current_w,pygame.display.Info().current_h))
			s_pantalla.fill((255,255,255))
			#---------------------------------------------------
			#actualizar los elementos insertados
			#Z2.objetos["div"]
			mapa=zu.mapear(Z2.orden,10)
			mapa.sort()
			#print "--------"
			#-----------------------------------------------------------
			#CREAR LAS SUPEFICIES
			c=0
			if renderizador==True:
				while c<=len(mapa)-1:
					indice=mapa[c][len(mapa[c])-1]
					#print indice,"$$$$"
					print mapa,"mapa"
					print indice
					app=Z2.obj_pygame[indice]
					if app.app=="DIV":
							app.css.update(s_pantalla)
							app.objetos["app"]["div"].funciones["export"](app)
							#print app.css.superficie,"::::::::"
							if app.css.get_style("position")!="absolute":
								print Z2.orden,"zorden"
								app.css.dibujar(Z2,zu.buscar_ruta(Z2.orden,indice,10,"padre"))
							
							
					c+=1
				renderizador=False
				
				
			for elem in Z2.orden.keys():
				s_pantalla.blit(Z2.obj_pygame[elem].css.superficie,(Z2.obj_pygame[elem].css.get_style("left"),Z2.obj_pygame[elem].css.get_style("top")))


			pygame.draw.polygon(s_pantalla,(255,255,255),[(random.randrange(200),random.randrange(200)),(random.randrange(200),random.randrange(200)),(random.randrange(200),random.randrange(200))])
			pantalla.blit(s_pantalla,(0,0))
			#---------------------------------------------------
			pygame.display.update() #actualizo el display
			
		pygame.quit()
		"""
#inserta los divs a la lista de objetos pygame
codigo2="""
		import copy
		Z2.obj_pygame.append(copy.deepcopy(Z2.objetos["app"]["DIV"]))
		Z2.orden[len(Z2.obj_pygame)-1]={}
		return len(Z2.obj_pygame)-1
		"""
#Anexa una superficie a otra
codigo3="""
		if Z2.obj_pygame[secundario].css.get_style("position")!="absolute":

			lista=Z2.orden[primario].keys()
			lista.sort()
			if lista !=[]:
				elemento=lista[len(lista)-1]
				if Z2.obj_pygame[elemento].css.get_style("display")=="block":
				    Z2.obj_pygame[secundario].css.pos_relativa[1]=Z2.obj_pygame[elemento].css.get_style("top")+Z2.obj_pygame[elemento].css.get_style("height")
				    
				if Z2.obj_pygame[elemento].css.get_style("display")=="inline":
					print "elemento", elemento
					Z2.obj_pygame[secundario].css.pos_relativa[0]=Z2.obj_pygame[elemento].css.get_style("left")+Z2.obj_pygame[elemento].css.get_style("width")
			Z2.orden[primario][secundario]={}	
			del Z2.orden[secundario]
			
			if Z2.obj_pygame[secundario].css.get_style("display")=="inline" and Z2.obj_pygame[secundario].app=="DIV" :
				del Z2.orden[primario][secundario]
				
			
		"""
'''
codigo2="""
		import copy
		Z2.obj_pygame.append(copy.deepcopy(Z2.objetos["app"]["DIV"]))
		Z2.orden[len(Z2.obj_pygame)-1]={}
		return len(Z2.obj_pygame)-1
		"""		
'''

Z2.fusionar(div.div)
Z2.fusionar(letra.letra)
Z2.cfuncion("main_pygame","Z2","es el motor de pygame para el modulo Z",codigo1)

Z2.obj_pygame=[]
Z2.orden={}
Z2.ejecutar=[]
Z2.cfuncion("DIV","Z2","crea un div",codigo2)
Z2.cfuncion("sobreponer",["Z2","primario","secundario"],"coloca un elemento encima de otro",codigo3)



#Z2.funciones["main_pygame"](Z2)
