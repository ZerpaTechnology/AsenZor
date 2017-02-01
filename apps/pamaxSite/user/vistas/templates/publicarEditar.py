#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html><head>	'''
incluir(data,"head")
print '''	'''
data["input"]="input"
print '''	'''
data["output"]="output"
print '''	'''
data["detalle"]=False
print '''</head><body class="container-fluid ff">'''
incluir(data,"header")
print ''''''
incluir(data,"publicarEditar")
print '''</body></html>'''