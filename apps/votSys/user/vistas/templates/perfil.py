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
print '''<section class="row"><div class="col-xs-12 col-sm-6 col-md-6 col-lg-6"><div class="pad-2"><h1>Actualizar perfil</h1><span>Foto Actual</span><br><img src="'''
print data['base_url']+'static/imgs/marker/partido-default.png'
print '''" class="shauto-20"><br><br><span>Foto a cambiar</span>'''
incluir(data,"previewImg-marco")
print '''</div></div><form class="col-xs-12 col-sm-6 col-md-6 col-lg-6" name="" id="perfil" ><div class="height-25 bg-ubuntu_ash pad-2" ><label>Nombres: </label><input type="text" name="" placeholder="Nombre"><br><label>Apellidos: </label><input type="text" name="" placeholder="Nombre"><br><label>Foto de perfil: </label>'''
incluir(data,"previewImg-boton")
print '''<br><label>Expediente: </label><input type="text" name="" placeholder="Nombre"><br><input type="submit" name="" value="Actualizar"></div></form></section>'''
incluir(data,"footer")
print '''</body></html>'''
