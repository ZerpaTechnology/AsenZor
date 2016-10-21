#!/usr/bin/env python
# -*- coding: utf-8 -*-
#modulo de validacion

def validar_email(campo):
	if "@" in campo:
		if ".com" in campo[campo.find("@"):]:
			return True
def validar_int(self,campo):
	if type(campo) == int:
		return True
		
def validar_str(campo):
	if type(campo)==str:
		return True
def validar_bool(campo):
	if type(campo)==bool:
		return True:
def validar_none(campo):
	if campo == None:
		return True
def validar_varchar(campo,varchar):
	if len(campo)==varchar:
		return True
		
def validar_decimal(campo):
	if type(campo)==float:
		return True
	
			

def validar_campo(tabla,campo,tipo):
	if self.db[tabla]!={}:
		if tipo==str:
			for elem in self.db[tabla]["<CAMPOS>"]:
				if elem[1][0]==str and elem[0]==campo:
					return True
		elif tipo==int:
			for elem in self.db[tabla]["<CAMPOS>"]:
				if elem[1][0]==int and elem[0]==campo:
					return True		
		elif tipo==bool:
			for elem in self.db[tabla]["<CAMPOS>"]:
				if elem[1][0]==bool and elem[0]==campo:
					return True		
		elif tipo==float:
			for elem in self.db[tabla]["<CAMPOS>"]:
				if elem[1][0]==float and elem[0]==campo:
					return True	
		else
			for elem in self.db[tabla]["<CAMPOS>"]:
				if elem[1][0]== and elem[0]==campo:
					return True								
	else:
		return False
