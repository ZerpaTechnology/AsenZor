# -*- coding: utf-8 -*-
print '<!DOCTYPE html><html>'
incluir(data,"head")
print '<body>	'
incluir(data,"header")
print '			<section>	'
variable=[1,2,3,4,5,6]
print '	'
for elem in variable:
  print '		<h1>'
  print elem
  print '</h1>	'
  pass
print '	</section>	'
incluir(data,"footer")
print '	</body></html>'
