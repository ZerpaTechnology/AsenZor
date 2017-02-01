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
print '''<section class="row"><div class="col-xs-12 col-sm-6 col-md-6 col-lg-6"><div class="pad-2"><h1>Inscribete</h1>'''
incluir(data,"previewImg-marco")
print '''<span> Nombre de la votación</span>	</div></div><form class="col-xs-12 col-sm-6 col-md-6 col-lg-6" name="form" id="registrar" action="post.py" method="post"><div class="height-25 bg-ubuntu_ash pad-2" ><label>Nombres: </label><input type="text" name="nombres" placeholder="Escribe tus nombres"><br><label>Apellidos: </label><input type="text" name="apellidos" placeholder="Escribe tus apellidos"><br><label>Correo: </label><input type="text" name="correo" placeholder="Escribe tu direccion de Email"><br><label>Contraseña: </label><input type="password" name="password" placeholder="Escribe tu Contraseña"><br><label>Foto de perfil: </label>'''
incluir(data,"previewImg-boton")
print '''<br><label>Expediente: </label><input type="text" name="expediente" placeholder="Escribe tu expediente"><br><input type="submit" name="" value="Registrarme"><input class="hidden" type="text" name="action" value="sing_up"></div></form></section>'''
incluir(data,"footer")
print '''</body></html>'''
