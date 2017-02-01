# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html>'''
incluir(data,"head")
print ''''''
data["detalle"]=False
print ''''''
data["input"]="btn1"
print ''''''
data["output"]="marco"
print '''<body class="container-fluid sin-marg pad-r08 pad-l08 ff">'''
incluir(data,"header")
print ''''''
incluir(data,"hero")
print ''''''
incluir(data,"barra-buscador")
print '''<section class="row"><div class="col-md-3"><h1>Crea tu votación</h1>'''
incluir(data,"previewImg-marco")
print '''<h5> Nombre de la votación</h5>	</div><div class="col-md-9 bg-ubuntu_ash pad-2"><form class="ff text-center" id="registroVotacion"><div>	<label>Nombre de la Votacion: </label>	<input type="text" name="" placeholder="Escribe tu nombre">	</div><div>	<h5>Foto de identificación: </h5>	'''
incluir(data,"previewImg-boton")
print '''		</div><input type="submit" name="" value="Registrarme" class="btn white"></form>	</div></section>'''
incluir(data,"footer")
print '''</body></html>'''
