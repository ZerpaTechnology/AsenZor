# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html>'''
incluir(data,"head")
print '''<body class="container-fluid sin-marg pad-r08 pad-l08 ff">'''
incluir(data,"header")
print '''<!--     -->'''
data["miembros"]=["pedro","juan","carlos","santiago"]
print ''''''
data["mision"]="""Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
print ''''''
data["vision"]="""Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
print '''<!--     -->'''
incluir(data,"hero")
print '''<div class="row"><div class="col-md-12"><div class="text-center bg-ubuntu_jet">	<div>		<input type="" name="" placeholder="Buscar partido">	</div></div><div>	</div><section class="row"><div class="col-md-8 text-center pad-2 b-s1"><h1>Nombre del partido</h1><img src="'''
print data['base_url']+'static/imgs/marker/partido-default.png'
print '''" class="shauto-20"><div><h1>Miembros</h1>	'''
for elem in data["miembros"]:
  print '''	<a href="">'''
  print elem,"<br>"
  print '''</a>'''
  pass
print '''</div><div>	</div><div class="text-justify marg-2"><h1 class="text-center">Misión</h1>'''
print data["mision"]
print '''	</div><div class="text-justify marg-2"><h1 class="text-center">Visión</h1>'''
print data["vision"]
print '''	</div><h1>Propuesta</h1><button>ver propuesta</button></div><div class="col-xs-12 col-md-4 text-center">	'''
incluir(data,"widget-chat")
print '''</div></section>'''
incluir(data,"footer")
print '''</body></html>'''
