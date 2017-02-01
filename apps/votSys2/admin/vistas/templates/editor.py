# -*- coding: utf-8 -*-
print '<!DOCTYPE html><html>'
incluir(data,"head")
print '<body class="AsenZor-admin ff"><div class="container-fluid">	<div class="row">		<div class="col-md-12">			'
incluir(data,"header")
print '		</div>		</div class="container">		<div class="row">		<div>			<div class="col-md-6">			<h1><b>Aplicaciones Instaladas</b></h1>			<h2><b>Producción</b></h2>			'
import os
print '			'
l=os.listdir(data["base_root"]+"../../")
print '			'
for elem in l:
  print '			<h3 class="marg-l2">'
  print elem
  print '</h3>			'
  pass
print '			<h2><b>Desarollo</b></h2>			'
l=os.listdir(config.base_root+config.projects_url)
print '			'
for elem in l:
  print '			<h3 class="marg-l2"><a href="'
  print config.base_url+'vista='+elem+'-edit&admin=True'
  print '">'
  print elem
  print '</a></h3>			'
  pass
print '			</div>			'
incluir(data,"dashboard-right")
print '		</div>		</div>	</div></div>'
incluir(data,"footer")
print '</body></html>'
