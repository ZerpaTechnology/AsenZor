# -*- coding: utf-8 -*-
print '<!DOCTYPE html><html>'
print '<head>	<meta charset="utf-8">		<title>Administrador</title>	<script src="'
print config.base_url
print 'static/js/jquery-3.1.1.min.js"></script>	<link rel="stylesheet" type="text/css" href="'
print config.base_url
print 'static/css/estilos.css">	<link rel="stylesheet" type="text/css" href="'
print config.base_url
print 'static/css/bootstrap.css">	<link rel="stylesheet" type="text/css" href="'
print config.base_url
print 'static/css/ff.css"></head>'



print '<body class="ff"><div class="container-fluid">	<div class="row">		<div class="col-md-12 text-center">			<div id="respuesta">							</div>			<form class="width-40 height-30 bg-ubuntu_orange" action="'
print config.base_url
print '" metod="post">			<div>			<label class="white">Libro</label>			<input type="hidden" name="form" value="consulta">				<input type="" name="libro" placeholder="Introduce el nombre del libro">				</div>			<div>			<label class="white">Tema</label>			<input type="text" name="tema" placeholder="Escribe el nombre del tema">				</div>			<div class="text-center">			<textarea placeholder=" Escribe el contenido" class="width-35" name="text" >							</textarea>				</div>						<input type="submit" name="enviar">		</form>			</div>			</div></div>'
print """<footer class="text-center bg-ubuntu_jet white pad-t1 pad-b1">
	zerpatechnlogy@2016
</footer>
<script type="text/javascript">
	$(document).ready(function() {
	$.ajax({
        type: 'POST',
        url: "post.py",
        data: {param: "prueba"}, //passing some input here
        dataType: "text",
        success: function(response){
           output = response;
           alert(output);
        }
}).done(function(data){
    console.log(data);
    alert(data);
});
	alert("hola");
	});
</script>"""


print '</body></html>'

