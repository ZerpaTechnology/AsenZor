#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import os
import time
import sys
sys.path.append("../config")
import config
sys.path.append("../"+config.libs_folder)
import ztec.intervalor.control
generar=ztec.intervalor.control.generar
archivo_act=sys.argv[0].split("/")[-1]

def darTipo(valor):
	exec("valor="+valor)
	return valor

for elem in config.libs:
	exec("import "+elem)

request=cgi.FieldStorage()


