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
print '''<section class="row"><div class="col-md-3"><h1>Inscribete</h1>'''
incluir(data,"previewImg-marco")
print '''<h5> Nombre de la votación</h5>	</div><div class="col-md-9 bg-ubuntu_ash"><form class="ff text-center" ><div>	<select>		<option>Academica</option>		<option>Popular</option>	</select></div><div>	<label>Nombres: </label>	<input type="text" name="" placeholder="Escribe tu nombre">	</div><div>	<label>Apellidos: </label>	<input type="text" name="" placeholder="Escribe tu apellido">	</div><div>	<label class="d-block">Nombre de la casa de estudio: </label>	<input type="text" name="" placeholder="Escribe el nombre de la institución donde estudias">	</div><div><label>Expediente: </label><input type="text" name="" placeholder="Escribe tu expediente ">	</div><div>	<h5>Foto de perfil: </h5>	'''
incluir(data,"previewImg-boton")
print '''		</div><input type="submit" name="" value="Registrarme" class="btn white"></form>	</div></section>'''
incluir(data,"footer")
print '''</body></html>'''
