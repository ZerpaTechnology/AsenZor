#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html>'''
incluir(data,"head")
print ''''''
data["detalle"]=False
print ''''''
data["output"]="marco"
print ''''''
data["input"]="btn"
print '''<body class="container-fluid sin-marg pad-r08 pad-l08 ff">'''
incluir(data,"header")
print ''''''
incluir(data,"hero")
print ''''''
incluir(data,"barra-buscador")
print '''<section class="row"><div class="col-xs-12 col-sm-6 col-md-6 col-lg-6"><div class="pad-2"><h1>Inscribete</h1>'''
incluir(data,"previewImg-marco")
print '''<span> Nombre de la votación</span>	</div></div><form class="col-xs-12 col-sm-6 col-md-6 col-lg-6" name="" id="login" action="post.py" method="post"><div class="height-25 bg-ubuntu_ash pad-2" ><label>correo: </label><input type="text" name="user" placeholder="Nombre"><br><label>password: </label><input type="password" name="password" placeholder="contraseña"><input type="password" name="action" value="sing_in" class="hidden"><br><input type="submit" name="" value="Entrar"></div></form></section>'''
incluir(data,"footer")
print '''</body></html>'''