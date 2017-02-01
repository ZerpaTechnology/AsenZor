#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html><head>	'''
incluir(data,"head")
print '''	'''
data["ultimasNoticias"]=["noticia1","noticia2","noticia3"]
print '''</head><body class="container-fluid ff">'''
incluir(data,"header")
print '''<section class="row"><div class="col-md-8 col-lg-8 col-xl-8"><div class="black">	<h1>Titulo</h1></div><img src=""><p>	Noticia</p><input id="datetimepicker" type="text" ><input type="number" name=""><input type="date" /></div><div class="col-md-4 col-lg-4 col-xl-8">'''
#incluir(data,"ultimasNoticias")
print ''''''+str(data["zform"])+''''''+str(FORM(DIV(_class="width-10 height-10 bg-ubuntu_jet")))+'''</div></section>'''
incluir(data,"footer")
print '''</body></html>'''