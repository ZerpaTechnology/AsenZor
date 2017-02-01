# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html>'''
incluir(data,"head")
print '''<body class="container-fluid sin-marg pad-r08 pad-l08 ff">'''
incluir(data,"header")
print ''''''
incluir(data,"hero")
print '''<section class="row"><div class="col-md-12"><div class="text-center bg-ubuntu_jet">	<div>		<input type="" name="" placeholder="Buscar votación">	</div></div><h1>Inscribete</h1><img src="'''
print data['base_url']+'static/imgs/marker/institucion-default.png'
print '''"><span> Nombre de la votación</span></div><form><label>Nombres: </label><input type="text" name="" placeholder="Nombre"><label>Apellidos: </label><input type="text" name="" placeholder="Nombre"><label>Foto de perfil: </label><input type="file" name="" placeholder="Nombre"><label>Expediente: </label><input type="text" name="" placeholder="Nombre"><input type="submit" name="" value="Registrarme"></form></section>'''
incluir(data,"footer")
print '''</body></html>'''
