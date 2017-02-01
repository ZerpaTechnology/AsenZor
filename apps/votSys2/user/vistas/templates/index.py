# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html>'''
incluir(data,"head")
print '''<body class="container-fluid sin-marg pad-r08 pad-l08 ff">'''
incluir(data,"header")
print ''''''
incluir(data,"hero")
print '''<section class="row"><div class="col-md-12"><div class="text-center bg-ubuntu_jet">	<div>		<input type="" name="" placeholder="Buscar votación">	</div></div><div class="text-center">'''
for elem in range(6):
  print '''	'''
  incluir(data,"widget-marker")
  print ''''''
  pass
print '''	</div></div>	</section>'''
incluir(data,"footer")
print '''<script type="text/javascript" src="'''
print config.base_url
print '''static/js/jquery-3.1.1.min.js"></script>'''
importar(data,"alert")
print '''</body></html>'''
