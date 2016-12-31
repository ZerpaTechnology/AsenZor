# -*- coding: utf-8 -*-
print '<!DOCTYPE html><html>'
incluir(data,"head")
print '<body class="AsenZor-admin ff"><div class="container-fluid">	'
incluir(data,"header")
print '		<section class="row"><div class="col-md-12 bg-ubuntu_orange"><h1>Necesitas Loguearte para continuar</h1><label>Usuario</label>	<input type="text" name="nick"><label>Contraseña</label>	<input type="password" name="password">	<input type="submit" name="entar" value="Entrar"></div></section>	'
incluir(data,"footer")
print '			</div></body></html>'
