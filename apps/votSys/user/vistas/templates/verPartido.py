# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html>'''
incluir(data,"head")
print '''<body class="container-fluid sin-marg pad-r08 pad-l08 ff">'''
incluir(data,"header")
print ''''''
incluir(data,"hero")
print '''<div class="row"><div class="col-md-12"><div class="text-center bg-ubuntu_jet">	<div>		<input type="" name="" placeholder="Buscar partido">	</div></div><div>	</div><section class="row"><div class="col-md-8 text-center" id="verPartido"><h1>Nombre de la Votacion</h1>'''
for elem in [1,1,1,1,1,1,1,1]:
  print '''	'''
  incluir(data,"widget-partido")
  print '''	'''
  pass
print '''</div><div class="col-md-4 text-center">	'''
incluir(data,"widget-chat")
print '''</div></section>'''
incluir(data,"footer")
print '''</body></html>'''
