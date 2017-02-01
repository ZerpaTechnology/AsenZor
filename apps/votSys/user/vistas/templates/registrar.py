#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html>'''
incluir(data,"head")
print ''''''
data["detalle"]=False
print ''''''
data["output"]="marco"
print ''''''
data["input"]="upload"
print '''<body class="container-fluid sin-marg pad-r08 pad-l08 ff">'''
incluir(data,"header")
print ''''''
incluir(data,"hero")
print ''''''
incluir(data,"barra-buscador")
print '''<section class="row"><div class="col-xs-12 col-sm-6 col-md-6 col-lg-6"><div class="pad-2"><h1>Registrarse</h1><p>Gracias por decidirte a usar nuestro sistema de votación</p></div></div><div class="col-xs-12 col-sm-6 col-md-6 col-lg-6">'''+str(data["zform"])+'''</div></section>'''
incluir(data,"footer")
print '''</body></html>'''