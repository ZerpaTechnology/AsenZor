#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html>'''
incluir(data,"head")
print ''''''
data["noticia-img"]=data["base_url"]+"static/img/noticia.jpg"
print ''''''
data["noticia-titulo"]="Pamax es un boomm.."
print ''''''
data["noticia-descripción"]="Pamax es un boomm.."
print '''<body class="container-fluid ff">'''
incluir(data,"header")
print ''''''
incluir(data,"noticiaFrame")
print '''</body></html>'''