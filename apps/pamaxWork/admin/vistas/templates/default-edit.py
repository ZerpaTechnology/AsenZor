# -*- coding: utf-8 -*-
print '<!DOCTYPE html><html>'
incluir(data,"head")
print '<body class="ff AsenZor-admin">'
incluir(data,"header")
print '<div class="container-fluid">	<div class="row">		<div class="col-md-12 text-center">			<div id="respuesta">							</div>			<form class="width-40 height-30 bg-ubuntu_orange" action="'
print config.base_url
print '" metod="post">			<div>			<label class="white">Libro</label>			<input type="hidden" name="form" value="consulta">				<input type="" name="libro" placeholder="Introduce el nombre del libro">				</div>			<div>			<label class="white">Tema</label>			<input type="text" name="tema" placeholder="Escribe el nombre del tema">				</div>			<div class="text-center">			<textarea placeholder=" Escribe el contenido" class="width-35" name="text" >							</textarea>				</div>						<input type="submit" name="enviar">		</form>			</div>			</div></div>'
incluir(data,"footer")
print '</body></html>'
